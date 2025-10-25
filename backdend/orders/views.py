from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer

class OrderListAPI(APIView):
    """
    处理订单列表的API：
    - GET：查询所有订单
    - POST：新增订单
    """
    def get(self, request):
        """查询所有订单（支持浏览器直接访问）"""
        orders = Order.objects.all()  # 从数据库查询所有订单
        serializer = OrderSerializer(orders, many=True)  # 序列化多个对象
        return Response(serializer.data)  # 返回JSON响应

    def post(self, request):
        """新增订单（需通过Postman等工具发送POST请求）"""
        # 验证请求数据并序列化
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():  # 数据验证通过
            serializer.save()  # 保存到数据库
            # 返回新增的订单数据，状态码201（创建成功）
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 验证失败返回错误信息，状态码400（请求错误）
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailAPI(APIView):
    """处理单个订单的API：GET查询指定ID的订单"""
    def get(self, request, pk):
        """根据ID查询订单（支持浏览器直接访问）"""
        try:
            order = Order.objects.get(pk=pk)  # 查询指定ID的订单
        except Order.DoesNotExist:  # 订单不存在
            return Response(status=status.HTTP_404_NOT_FOUND)  # 返回404
        serializer = OrderSerializer(order)  # 序列化单个对象
        return Response(serializer.data)  # 返回订单详情