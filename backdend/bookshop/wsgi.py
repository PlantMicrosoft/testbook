import os  # 导入操作系统相关模块，用于环境变量设置
from django.core.wsgi import get_wsgi_application  # 导入Django的WSGI应用生成函数

# 设置Django配置模块的环境变量，指定项目使用的settings文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookshop.settings')
# 创建WSGI应用对象，供WSGI服务器（如Gunicorn、uWSGI）调用，处理HTTP请求
application = get_wsgi_application()