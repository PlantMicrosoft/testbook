from django.db import models  # 导入Django模型基类
from django.utils import timezone  # 导入时间工具，用于处理时间字段

class Order(models.Model):  # 定义订单模型，继承models.Model（Django模型基类）
    """订单实体类，对应数据库t_order表"""
    # 商品名称：字符串类型，最大长度255，verbose_name为后台显示名称
    product_name = models.CharField(max_length=255, verbose_name="商品名称")
    # 购买数量：整数类型
    quantity = models.IntegerField(verbose_name="购买数量")
    # 订单总价： decimal类型，总位数10，小数位数2（支持最大9999999.99）
    total_price = models.DecimalField(
        max_digits=10,  # 总位数（整数+小数）
        decimal_places=2,  # 小数位数
        verbose_name="订单总价"
    )
    # 客户姓名：字符串类型，最大长度100
    customer_name = models.CharField(max_length=100, verbose_name="客户姓名")
    # 创建时间：日期时间类型，默认值为当前时间（timezone.now）
    create_time = models.DateTimeField(
        default=timezone.now,  # 默认值
        verbose_name="创建时间"
    )

    class Meta:  # 模型元数据，配置数据库表相关信息
        db_table = "t_order"  # 数据库表名（默认为app名_模型名，这里自定义为t_order）
        verbose_name = "订单"  # 后台显示的模型名称（单数）
        verbose_name_plural = verbose_name  # 后台显示的模型名称（复数，与单数相同）

    def __str__(self):  # 定义对象的字符串表示
        """对象字符串表示，用于后台显示和调试"""
        return f"{self.customer_name}的订单：{self.product_name}"