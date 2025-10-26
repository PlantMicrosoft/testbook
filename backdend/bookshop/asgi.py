import os  # 导入操作系统相关模块
from django.core.asgi import get_asgi_application  # 导入Django的ASGI应用生成函数

# 设置Django配置模块的环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookshop.settings')
# 创建ASGI应用对象，支持异步通信的Web服务器（如Uvicorn）调用
application = get_asgi_application()