from django.urls import path
from .views import OrderListAPI, OrderDetailAPI

# 订单相关API路由
urlpatterns = [
    # 列表路由：GET查询所有 / POST新增
    path('api/orders/', OrderListAPI.as_view(), name='order-list'),
    # 详情路由：GET查询单个（pk为订单ID）
    path('api/orders/<int:pk>/', OrderDetailAPI.as_view(), name='order-detail'),
]