from django.contrib import admin  # 导入Django自带的admin后台模块
from django.urls import path, include  # 导入路由相关工具：path定义路由，include用于包含其他路由

# 定义项目全局路由列表
urlpatterns = [
    path('admin/', admin.site.urls),  # 配置Django Admin后台的访问路径（/admin）
    path('', include('orders.urls')),  # 包含orders应用的路由配置，将空路径（/）转发给orders.urls处理
]