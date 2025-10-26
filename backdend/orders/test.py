from django.test import TestCase  # 导入Django测试基类
from django.urls import reverse  # 导入reverse函数，用于通过路由名称生成URL
from rest_framework.test import APIClient  # 导入DRF的API测试客户端，模拟HTTP请求
from rest_framework import status  # 导入状态码模块，用于断言响应状态
from .models import Order  # 导入Order模型，用于测试数据的创建和查询
import json  # 导入json模块，用于处理JSON数据

class OrderAPITest(TestCase):
    """订单API的单元测试"""
    def setUp(self):
        """测试前初始化数据（每个测试方法执行前都会调用）"""
        self.client = APIClient()  # 初始化API测试客户端
        # 创建测试订单1
        self.order1 = Order.objects.create(
            product_name="Python编程",
            quantity=2,
            total_price=99.80,
            customer_name="张三"
        )
        # 创建测试订单2
        self.order2 = Order.objects.create(
            product_name="Django实战",
            quantity=1,
            total_price=89.00,
            customer_name="李四"
        )
        # 获取API路径（通过路由名称生成URL，避免硬编码）
        self.list_url = reverse('order-list')  # 订单列表API路径：/api/orders/
        self.detail_url = reverse('order-detail', args=[self.order1.id])  # 订单详情API路径：/api/orders/1/

    def test_get_all_orders(self):
        """测试查询所有订单的API"""
        response = self.client.get(self.list_url)  # 发送GET请求到列表API
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 断言响应状态码为200（成功）
        self.assertEqual(len(response.data), 2)  # 断言返回的数据条数为2（与setUp中创建的订单数一致）

    def test_get_order_by_id(self):
        """测试查询单个订单的API"""
        response = self.client.get(self.detail_url)  # 发送GET请求到详情API
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 断言状态码为200
        self.assertEqual(response.data['product_name'], "Python编程")  # 断言返回的商品名称正确

    def test_create_order(self):
        """测试新增订单的API"""
        # 准备新增订单的数据
        new_order_data = {
            "product_name": "Flask入门",
            "quantity": 3,
            "total_price": 120.00,
            "customer_name": "王五"
        }
        # 发送POST请求（需指定content_type为application/json，数据转为JSON字符串）
        response = self.client.post(
            self.list_url,
            data=json.dumps(new_order_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # 断言状态码为201（创建成功）
        self.assertEqual(Order.objects.count(), 3)  # 断言数据库中订单总数为3（原2条+新增1条）