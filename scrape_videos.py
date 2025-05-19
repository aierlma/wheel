#!/usr/bin/env python3
"""
scrape_videos.py

从 https://xxxx.com/all-videos/ 页面及其所有分页中提取视频页面链接及封面图，
保存链接到 video_links.txt，将封面图下载并转换为 PNG，命名为 <slug>.png（Emby 可识别格式）。
"""

import os
import requests
from io import BytesIO
from bs4 import BeautifulSoup
import imageio
from PIL import Image
import re

def fetch_all_video_items(base_url):
    """
    遍历所有分页，收集视频页面链接和对应缩略图 URL。
    返回：列表，元素为 (video_url, thumbnail_url)。
    """
    # 获取最大页码
    resp = requests.get(base_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    page_numbers = [int(a.get_text(strip=True)) for a in soup.find_all('a', class_='page-numbers') if a.get_text(strip=True).isdigit()]
    max_page = max(page_numbers) if page_numbers else 1

    items = []
    seen = set()

    for page in range(1, max_page + 1):
        url = base_url if page == 1 else base_url.rstrip('/') + f'/page/{page}/'
        print(f'Fetching page {page}/{max_page}: {url}')
        resp = requests.get(url); resp.raise_for_status()
        page_soup = BeautifulSoup(resp.text, 'html.parser')

        for div in page_soup.find_all('div', class_='half'):
            center = div.find('center', class_='vidcont')
            if not center: continue
            a = center.find('a', href=True)
            img = center.find('img', src=True)
            if a and img:
                video_url = a['href'].strip()
                # 选择 srcset 中最大尺寸，若无则取 src
                src = img.get('src', '').strip()
                srcset = img.get('srcset', '').strip()
                if srcset:
                    candidates = [token.strip().split(' ')[0] for token in srcset.split(',')]
                    thumb_url = candidates[-1]
                else:
                    thumb_url = src
                if video_url not in seen:
                    seen.add(video_url)
                    items.append((video_url, thumb_url))
    return items

def save_links(items, path):
    """将所有视频链接写入文本文件，每行一个链接。"""
    with open(path, 'w', encoding='utf-8') as f:
        for url, _ in items:
            f.write(url + '\n')
    print(f'Links saved to: {path}')

def download_and_convert_thumbs(items, out_dir):
    """下载所有缩略图并转换为 PNG，按 slug 命名保存在 out_dir，只处理不存在的文件。"""
    os.makedirs(out_dir, exist_ok=True)
    failed = []
    for video_url, thumb_url in items:
        slug = video_url.rstrip('/').split('/')[-1]
        out_path = os.path.join(out_dir, f'{slug}.png')
        if os.path.exists(out_path):
            print(f'Skipping existing thumbnail: {out_path}')
            continue
        try:
            resp = requests.get(thumb_url)
            resp.raise_for_status()
            buf = BytesIO(resp.content)
            # 尝试 PIL 打开
            try:
                img = Image.open(buf).convert('RGBA')
            except Exception:
                # fallback 使用 imageio.v2 处理 WEBP/AVIF
                buf.seek(0)
                arr = imageio.v2.imread(buf)
                img = Image.fromarray(arr).convert('RGBA')
            img.save(out_path, format='PNG')
            print(f'Saved thumbnail: {out_path}')
        except Exception as e:
            print(f'Failed {slug}: {e}')
            # 尝试替换 .webp 扩展名为 .png 重试
            alt_url = thumb_url.rsplit('.', 1)[0] + '.png'
            try:
                resp2 = requests.get(alt_url)
                resp2.raise_for_status()
                buf2 = BytesIO(resp2.content)
                try:
                    img2 = Image.open(buf2).convert('RGBA')
                except Exception:
                    buf2.seek(0)
                    arr = imageio.v2.imread(buf2)
                    img2 = Image.fromarray(arr).convert('RGBA')
                img2.save(out_path, format='PNG')
                print(f'Saved alt thumbnail from PNG: {out_path}')
                continue
            except Exception as e2:
                print(f'Alt URL failed for {slug}: {e2}')
            # 尝试获取原始尺寸 webp
            full_url = re.sub(r'-\\d+x\\d+(?=\\.)', '', thumb_url)
            try:
                resp_f = requests.get(full_url)
                resp_f.raise_for_status()
                buf_f = BytesIO(resp_f.content)
                try:
                    img_f = Image.open(buf_f).convert('RGBA')
                except Exception:
                    buf_f.seek(0)
                    arr = imageio.v2.imread(buf_f)
                    img_f = Image.fromarray(arr).convert('RGBA')
                img_f.save(out_path, format='PNG')
                print(f'Saved full-size thumbnail: {out_path}')
                continue
            except Exception as e_full:
                print(f'Full-size URL failed for {slug}: {e_full}')
            # 尝试从视频页面的 og:image 获取封面
            try:
                page_resp = requests.get(video_url)
                page_resp.raise_for_status()
                page_soup = BeautifulSoup(page_resp.text, 'html.parser')
                og = page_soup.find('meta', property='og:image')
                if og and og.get('content'):
                    og_url = og['content']
                    resp3 = requests.get(og_url)
                    resp3.raise_for_status()
                    buf3 = BytesIO(resp3.content)
                    img3 = Image.open(buf3).convert('RGBA')
                    img3.save(out_path, format='PNG')
                    print(f'Saved OG thumbnail: {out_path}')
                    continue
            except Exception as e3:
                print(f'OG image failed for {slug}: {e3}')
            # 最后尝试保存原始文件
            try:
                ext = os.path.splitext(thumb_url)[1].split('?')[0]
                raw_path = os.path.join(out_dir, f'{slug}{ext}')
                with open(raw_path, 'wb') as rf:
                    rf.write(resp.content)
                print(f'Saved raw thumbnail: {raw_path}')
            except Exception as e4:
                print(f'Also failed raw save {slug}: {e4}')
            failed.append(slug)
    if failed:
        print(f'Failed thumbnails: {", ".join(failed)}')

def main():
    base_url = 'https://xxx.com/all-videos/'
    print('开始抓取所有分页的视频链接和封面图...\n')
    items = fetch_all_video_items(base_url)
    if not items:
        print('未找到任何视频项目。')
        return
    save_links(items, 'video_links.txt')
    download_and_convert_thumbs(items, 'thumbnails')

if __name__ == '__main__':
    main()
