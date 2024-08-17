import requests
import json


# EmbyClient类用于封装与Emby服务器交互的逻辑
class EmbyClient:
    def __init__(self, server_ip, user_id, api_key, port=8096):
        # 初始化时设置服务器IP地址、用户ID和API密钥
        self.server_ip = server_ip
        self.user_id = user_id
        self.api_key = api_key
        self.port = port
        # 构建Emby服务器的基本URL
        self.emby_url = f"http://{self.server_ip}:{self.port}"
    
    def _send_request(self, endpoint):
        """
        私有方法，用于发送HTTP请求并处理响应。
        """
        # 构建完整的URL，包括API密钥
        url = f"{self.emby_url}{endpoint}&api_key={self.api_key}"
        try:
            # 发送GET请求
            response = requests.get(url)
            # 检查是否有HTTP错误
            response.raise_for_status()
            # 返回JSON格式的数据
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            # 捕捉并打印HTTP错误
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            # 捕捉并打印其他异常
            print(f"An error occurred: {err}")
        # 如果出现异常，返回None
        return None

    def get_favorite_movies(self):
        """
        获取标记为“最爱”的电影并保存到JSON文件中。
        """
        # 构建用于获取“最爱”电影的API端点
        endpoint = f"/emby/Users/{self.user_id}/Items?IsFavorite=true&IncludeItemTypes=Movie&Recursive=true"
        # 发送请求并获取数据
        data = self._send_request(endpoint)
        if data:
            # 提取电影的详细信息
            favorite_details = [{
                'Name': item['Name'],
                'Type': item['Type'],
                'Id': item['Id']
            } for item in data.get('Items', [])]
            # 将提取到的数据保存到文件中
            self._save_to_file(favorite_details, 'emby_favorites_movies.json')
            print("“最爱”电影数据已备份到 emby_favorites_movies.json")
        else:
            # 如果请求失败，打印提示信息
            print("未能获取“最爱”电影数据。")
    
    def get_collection_items(self, collection_ids):
        """
        获取多个合集中的项目，并根据合集ID分类保存到JSON文件中。
        """
        all_collections = {}
        
        # 遍历每个合集ID
        for collection_id in collection_ids:
            # 构建用于获取合集项目的API端点
            endpoint = f"/emby/Users/{self.user_id}/Items?ParentId={collection_id}"
            # 发送请求并获取数据
            data = self._send_request(endpoint)
            
            if data:
                # 提取每个合集中的项目
                items = data.get('Items', [])
                
                # 将项目列表存储在以 collection_id 为键的字典中
                all_collections[collection_id] = [{
                    'Name': item['Name'],
                    'Type': item['Type'],
                    'Id': item['Id']
                } for item in items]
            else:
                # 如果请求失败，打印提示信息
                print(f"未能获取合集ID为 {collection_id} 的项目数据。")
        
        # 将所有按合集ID分类的项目保存到文件中
        self._save_to_file(all_collections, 'emby_collections_items.json')
        print("所有合集中的项目数据已按合集ID分类备份到 emby_collections_items.json")

    @staticmethod
    def _save_to_file(data, filename):
        """
        静态方法，用于将数据保存到JSON文件中。
        """
        # 以UTF-8编码打开文件，并写入JSON数据
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


# 使用示例
if __name__ == "__main__":
    # 创建EmbyClient对象，传入服务器IP、用户ID和API密钥
    emby_client = EmbyClient(
        server_ip="192.168.110.237",
        user_id="25f9703b863c47dba7b359fb7421c68b",
        api_key="30f77d540fb84d69b9c52bb92f81bdb4"
    )
    
    # 获取并保存“最爱”电影
    emby_client.get_favorite_movies()
    
    # 获取并保存多个合集中的项目
    collection_ids = ['3253', '4202']
    emby_client.get_collection_items(collection_ids)
