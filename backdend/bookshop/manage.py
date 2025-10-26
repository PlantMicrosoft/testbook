#!/usr/bin/env python  # 指定脚本解释器为Python
"""Django's command-line utility for administrative tasks."""  # 文档字符串：说明这是Django的管理任务工具
import os  # 导入操作系统模块
import sys  # 导入系统相关模块

def main():
    """Run administrative tasks."""  # 函数说明：执行管理任务
    # 设置Django配置模块的环境变量
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookshop.settings')
    try:
        # 导入Django的命令行执行函数
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # 处理导入失败异常（如未安装Django或未激活虚拟环境）
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 执行命令行传入的指令（如runserver、migrate等）
    execute_from_command_line(sys.argv)

'''Django 项目的命令行管理工具，用于执行各种 administrative 任务，
如启动开发服务器（python manage.py runserver）、
数据库迁移（python manage.py migrate）、
创建超级用户（python manage.py createsuperuser）等。'''
# 当脚本直接运行时（而非被导入），执行main函数
if __name__ == '__main__':
    main()