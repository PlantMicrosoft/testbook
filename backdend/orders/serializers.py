from rest_framework import serializers  # 导入DRF的序列化器模块
from .models import Order  # 导入Order模型

class OrderSerializer(serializers.ModelSerializer):  # 定义订单序列化器，继承ModelSerializer（自动映射模型字段）
    """订单序列化器，用于API请求/响应的数据转换"""
    class Meta:  # 元数据类，配置序列化器与模型的映射关系
        model = Order  # 关联的模型（映射Order模型）
        # 需序列化的字段（API请求/响应中包含的字段）
        fields = ['id', 'product_name', 'quantity', 'total_price', 'customer_name', 'create_time']
        # 只读字段（不允许前端通过API修改，由后端自动生成/维护）
        read_only_fields = ['id', 'create_time']  # id自增，create_time自动生成，前端无需传递