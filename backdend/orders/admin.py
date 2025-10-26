from django.contrib import admin  # 导入Django Admin模块
from .models import Order  # 导入Order模型

@admin.register(Order)  # 注册Order模型到Admin，等价于admin.site.register(Order, OrderAdmin)
class OrderAdmin(admin.ModelAdmin):  # 定义订单模型的Admin管理类
    """在Django Admin中注册订单模型，支持后台可视化管理"""
    # 列表页显示的字段（后台列表页可见的列）
    list_display = ['id', 'product_name', 'quantity', 'total_price', 'customer_name', 'create_time']
    # 可搜索的字段（后台顶部搜索框可搜索的列）
    search_fields = ['product_name', 'customer_name']
    # 可筛选的字段（右侧筛选器可根据该字段过滤）
    list_filter = ['create_time']
    # 排序字段（默认按创建时间倒序，-表示降序）
    ordering = ['-create_time']