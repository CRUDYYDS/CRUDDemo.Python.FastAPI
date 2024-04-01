# 快速启动指南

#### 1.装依赖
```
pip install -r requirements.txt
```

#### 2.创建一个名为postgres的数据库

#### 3.修改db.py中的数据库连接字符串 SQLALCHEMY_DATABASE_URL 以及 alembic/env.py中的 sqlalchemy.url

#### 4.生成迁移脚本
```
alembic revision --autogenerate -m "initial_create" 
```

#### 5.应用迁移脚本
```
alembic upgrade head
```

#### 6.运行
```
uvicorn main:app --reload
```

#### 7.浏览器中查看并测试接口
http://localhost:8000/docs
