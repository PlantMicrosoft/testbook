from django.db import models
from django.utils import timezone

class Order(models.Model):
    """订单实体类，对应数据库t_order表"""
    product_name = models.CharField(max_length=255, verbose_name="商品名称")  # 非空字符串
    quantity = models.IntegerField(verbose_name="购买数量")  # 整数
    total_price = models.DecimalField(
        max_digits=10,  # 总位数
        decimal_places=2,  # 小数位数
        verbose_name="订单总价"
    )
    customer_name = models.CharField(max_length=100, verbose_name="客户姓名")
    create_time = models.DateTimeField(
        default=timezone.now,  # 默认值为当前时间
        verbose_name="创建时间"
    )

    class Meta:
        db_table = "t_order"  # 数据库表名
        verbose_name = "订单"  # 后台显示名称
        verbose_name_plural = verbose_name  # 复数形式

    def __str__(self):
        """对象字符串表示，用于后台显示"""
        return f"{self.customer_name}的订单：{self.product_name}"