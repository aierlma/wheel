#!/bin/bash

# 配置域名和端口
services=(
  # "aaa.example.com:3000"
  # "bbb.example.top:5244"
  # "ccc.example.xyz:19798"
  "eee.example.org:8097"
)

# 安装必要的软件
sudo apt update
sudo apt install -y nginx certbot python3-certbot-nginx

# 创建 Nginx 配置并申请证书
for service in "${services[@]}"; do
  domain=$(echo "$service" | cut -d: -f1)
  port=$(echo "$service" | cut -d: -f2)

  # 创建 Nginx 配置文件
  cat <<EOF | sudo tee /etc/nginx/sites-available/$domain
server {
    listen 80;
    listen [::]:80;
    server_name $domain;

    location /.well-known/acme-challenge {
        root /var/www/html;
    }

    location / {
        proxy_pass http://localhost:$port;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

  # 创建符号链接并测试 Nginx
  sudo ln -s /etc/nginx/sites-available/$domain /etc/nginx/sites-enabled/
  sudo nginx -t
  sudo systemctl reload nginx

  # 使用 Certbot 申请 SSL 证书
  sudo certbot certonly --nginx -d $domain --email aierlma521@gmail.com --agree-tos --non-interactive

  # 更新 Nginx 配置文件以启用 HTTPS
  cat <<EOF | sudo tee /etc/nginx/sites-available/$domain
server {
    listen 80;
    listen [::]:80;
    server_name $domain;
    return 301 https://\$server_name\$request_uri;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name $domain;

    ssl_certificate /etc/letsencrypt/live/$domain/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$domain/privkey.pem;

    location / {
        proxy_pass http://localhost:$port;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

  # 测试并重启 Nginx
  sudo nginx -t
  sudo systemctl reload nginx

done

# 输出完成消息
echo "所有服务的 Nginx 配置和 SSL 证书已成功设置！"
