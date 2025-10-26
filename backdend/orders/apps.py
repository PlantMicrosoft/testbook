from django.apps import AppConfig  # 导入Django应用配置基类

class OrdersConfig(AppConfig):  # 定义订单应用的配置类
    default_auto_field = 'django.db.models.BigAutoField'  # 设置默认主键类型为BigAutoField（大整数自增）
    name = 'orders'  # 应用名称，必须与settings.py中INSTALLED_APPS注册的名称一致