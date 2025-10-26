import os  # 导入操作系统模块
from pathlib import Path  # 导入路径处理模块

# 项目根目录：当前文件所在目录的父目录（bookshop项目根目录）
BASE_DIR = Path(__file__).resolve().parent.parent

# 安全密钥：用于Django的加密签名（如会话cookie、CSRF令牌等），生产环境需替换为随机字符串
SECRET_KEY = 'django-insecure-example-key-for-development-only'

# DEBUG模式：开发环境设为True（显示详细错误信息），生产环境必须设为False
DEBUG = True

# 允许访问的主机：开发环境允许localhost和127.0.0.1访问
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# 安装的应用：项目中启用的Django应用和第三方库
INSTALLED_APPS = [
    'django.contrib.admin',  # Django自带的后台管理应用
    'django.contrib.auth',  # 身份认证系统
    'django.contrib.contenttypes',  # 内容类型框架（用于权限管理）
    'django.contrib.sessions',  # 会话管理
    'django.contrib.messages',  # 消息提示框架
    'django.contrib.staticfiles',  # 静态文件管理
    'rest_framework',  # 注册Django REST Framework（DRF）框架，用于构建API
    'orders',  # 注册自定义的订单业务应用
]

# 中间件：请求/响应处理的钩子函数，按顺序执行（如安全验证、会话管理、CSRF保护等）
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # 安全相关中间件（如HTTPS重定向）
    'django.contrib.sessions.middleware.SessionMiddleware',  # 会话管理中间件
    'django.middleware.common.CommonMiddleware',  # 通用中间件（如URL重定向）
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF保护中间件
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 身份认证中间件
    'django.contrib.messages.middleware.MessageMiddleware',  # 消息提示中间件
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # 防止点击劫持的中间件
]

# 主路由配置：指定项目的主路由模块
ROOT_URLCONF = 'bookshop.urls'

# 模板配置：定义模板引擎和查找路径（前后端分离项目可忽略）
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # 使用Django自带模板引擎
        'DIRS': [],  # 模板文件的额外查找目录（空表示仅使用应用内的templates目录）
        'APP_DIRS': True,  # 是否搜索应用内的templates目录
        'OPTIONS': {
            'context_processors': [  # 模板上下文处理器（提供全局变量）
                'django.template.context_processors.debug',  # 调试相关上下文
                'django.template.context_processors.request',  # 请求对象（request）
                'django.contrib.auth.context_processors.auth',  # 认证相关上下文
                'django.contrib.messages.context_processors.messages',  # 消息提示上下文
            ],
        },
    },
]

# WSGI应用配置：指定WSGI应用对象的路径
WSGI_APPLICATION = 'bookshop.wsgi.application'

# 数据库配置：使用MySQL数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎（MySQL）
        'NAME': 'ecommerce_db',  # 数据库名（需提前手动创建）
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库密码
        'HOST': 'localhost',  # 数据库主机地址
        'PORT': '3306',  # 数据库端口
        'OPTIONS': {'charset': 'utf8mb4'},  # 字符集（支持emoji等特殊字符）
    }
}

# 密码验证器：定义密码强度验证规则
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # 密码与用户属性相似度验证
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # 密码最小长度验证
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # 常见密码验证（如123456）
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # 纯数字密码验证
]

# 国际化配置
LANGUAGE_CODE = 'en-us'  # 语言（默认英语）
TIME_ZONE = 'UTC'  # 时区（默认UTC）
USE_I18N = True  # 启用国际化
USE_TZ = True  # 启用时区支持

# 静态文件配置：静态文件（CSS、JS等）的URL前缀（前后端分离项目可忽略）
STATIC_URL = 'static/'
# 默认主键类型：模型默认使用BigAutoField（自增bigint）
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF全局配置：Django REST Framework的全局设置
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # 默认分页类
    'PAGE_SIZE': 10,  # 每页数据量
}