from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    """订单序列化器，用于API请求/响应的数据转换"""
    class Meta:
        model = Order  # 关联的模型
        # 需序列化的字段（与前端交互的字段）
        fields = ['id', 'product_name', 'quantity', 'total_price', 'customer_name', 'create_time']
        # 只读字段（ID自增，创建时间自动生成，不允许前端修改）
        read_only_fields = ['id', 'create_time']