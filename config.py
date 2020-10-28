#!/usr/bin/env python

# DataBase Config
mysql = {'host': 'localhost',
         'user': 'root',
         'passwd': 'root',
         'db': 'arcane'}


mysqlConfig = "mysql+pymysql://{}:{}@{}/{}".format(mysql['user'], mysql['passwd'], mysql['host'], mysql['db'])
