# 使用Python 3.11作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制requirements.txt文件并安装依赖
#COPY requirements.txt .
RUN pip install xiyan-mcp-server
# 复制应用代码
#COPY . .

# 暴露端口（如果需要）
# EXPOSE 5000

# 运行应用
CMD ["python", "-m", "xiyan_mcp_server"]