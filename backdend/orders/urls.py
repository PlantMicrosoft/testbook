from django.urls import path  # 导入Django的path函数，用于定义URL路由
from .views import OrderListAPI, OrderDetailAPI  # 导入视图类

# 订单相关API路由列表
urlpatterns = [
    # 列表路由：GET请求查询所有订单，POST请求新增订单，路径为/api/orders/
    path('api/orders/', OrderListAPI.as_view(), name='order-list'),
    # 详情路由：GET请求查询单个订单（pk为订单ID），路径为/api/orders/<id>/
    path('api/orders/<int:pk>/', OrderDetailAPI.as_view(), name='order-detail'),
]