from rest_framework.views import APIView  # 导入DRF的APIView基类，用于构建基于类的视图
from rest_framework.response import Response  # 导入Response类，用于返回HTTP响应
from rest_framework import status  # 导入状态码模块，包含HTTP状态码常量
from .models import Order  # 导入当前应用的Order模型，用于数据库操作
from .serializers import OrderSerializer  # 导入OrderSerializer，用于数据序列化/反序列化

class OrderListAPI(APIView):  # 定义处理订单列表的视图类，继承APIView
    """
    处理订单列表的API：
    - GET：查询所有订单
    - POST：新增订单
    """
    def get(self, request):  # 定义GET请求处理方法
        """查询所有订单（支持浏览器直接访问）"""
        orders = Order.objects.all()  # 从数据库查询所有订单记录
        serializer = OrderSerializer(orders, many=True)  # 序列化多个订单对象（many=True表示多对象）
        return Response(serializer.data)  # 返回序列化后的JSON数据

    def post(self, request):  # 定义POST请求处理方法
        """新增订单（需通过Postman等工具发送POST请求）"""
        # 用请求数据初始化序列化器，进行数据验证
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():  # 检查数据是否验证通过
            serializer.save()  # 验证通过则保存数据到数据库
            # 返回新增的订单数据，状态码201（表示资源创建成功）
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 验证失败返回错误信息，状态码400（表示请求参数错误）
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailAPI(APIView):  # 定义处理单个订单的视图类
    """处理单个订单的API：GET查询指定ID的订单"""
    def get(self, request, pk):  # 定义GET请求处理方法，pk为订单ID
        """根据ID查询订单（支持浏览器直接访问）"""
        try:
            order = Order.objects.get(pk=pk)  # 根据ID查询单个订单
        except Order.DoesNotExist:  # 捕获订单不存在的异常
            return Response(status=status.HTTP_404_NOT_FOUND)  # 返回404状态码（资源不存在）
        serializer = OrderSerializer(order)  # 序列化单个订单对象
        return Response(serializer.data)  # 返回订单详情数据