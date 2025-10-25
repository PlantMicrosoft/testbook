from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Order
import json

class OrderAPITest(TestCase):
    """订单API的单元测试"""
    def setUp(self):
        """测试前初始化数据"""
        self.client = APIClient()  # API测试客户端
        # 创建测试订单
        self.order1 = Order.objects.create(
            product_name="Python编程",
            quantity=2,
            total_price=99.80,
            customer_name="张三"
        )
        self.order2 = Order.objects.create(
            product_name="Django实战",
            quantity=1,
            total_price=89.00,
            customer_name="李四"
        )
        # API路径
        self.list_url = reverse('order-list')  # /api/orders/
        self.detail_url = reverse('order-detail', args=[self.order1.id])  # /api/orders/1/

    def test_get_all_orders(self):
        """测试查询所有订单"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # 应返回2条数据

    def test_get_order_by_id(self):
        """测试查询单个订单"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product_name'], "Python编程")

    def test_create_order(self):
        """测试新增订单"""
        new_order_data = {
            "product_name": "Flask入门",
            "quantity": 3,
            "total_price": 120.00,
            "customer_name": "王五"
        }
        response = self.client.post(
            self.list_url,
            data=json.dumps(new_order_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 3)  # 数据库应新增1条数据