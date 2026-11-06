# 使用官方 Python 3.10 精簡版
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 安裝系統依賴套件（包含 Chromium 與其 Driver，供 Selenium 使用）
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    unzip \
    chromium \
    chromium-driver \
    libglib2.0-0 \
    libnss3 \
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

# 設定 Selenium 使用的瀏覽器環境變數
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案其餘檔案到容器內
COPY . .

# 建立 instance 資料夾供 SQLite 存放
RUN mkdir -p instance

# 暴露 Flask 預設連接埠
EXPOSE 4000

# 啟動應用程式
CMD ["python3", "main.py"]