import pymysql  # 导入pymysql库（Python连接MySQL的驱动）
# 将pymysql伪装成MySQLdb，因为Django默认使用MySQLdb连接MySQL，但Python3中常用pymysql
pymysql.install_as_MySQLdb()
'''模块作用：__init__.py标识该目录为 Python 包。
此处主要解决 Django 与 MySQL 的兼容问题：
Django 原生依赖MySQLdb，但MySQLdb不支持 Python3，
通过pymysql.install_as_MySQLdb()让 Django 
使用pymysql替代MySQLdb连接 MySQL。'''