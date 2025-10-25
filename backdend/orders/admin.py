from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """在Django Admin中注册订单模型，支持后台可视化管理"""
    # 列表页显示的字段
    list_display = ['id', 'product_name', 'quantity', 'total_price', 'customer_name', 'create_time']
    # 可搜索的字段
    search_fields = ['product_name', 'customer_name']
    # 可筛选的字段
    list_filter = ['create_time']
    # 排序字段（默认按创建时间倒序）
    ordering = ['-create_time']