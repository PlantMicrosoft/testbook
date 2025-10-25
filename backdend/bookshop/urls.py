from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin后台路由
    path('', include('orders.urls')),  # 包含订单模块的路由
]