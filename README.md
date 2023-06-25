# 基于django+REST framework+simpleui+vue2 开发运维系统

## 接口调用
以下文档都是由django 自动生成不需要自己去维护

###  api 文档  
http://127.0.0.1:9090/redoc/

###  swagger  
http://127.0.0.1:9090/swagger/


###   Django REST framework  类似postmain 可以在线调试

http://127.0.0.1:9090/app名/

例如

http://127.0.0.1:9090/ConfCen/ 




## 基于django admin 在页面添加一个 可增删改查的页面 和自定义个功能模块


## 基于vue 自定义一个页面

## 基于 django template 自定义一个页面


## 基于REST framework 自定义一个接口 可增删改查的接口 和自定义个功能模块

## 基于REST framework  自定义一个接口



## 运维系统架构体系


# 基于这个架构体系实现 一个任务
配置中心加一个 配置

如 cloud7

配置如下

name: cloud7
git: xxxx
info : 
- hello 
- world 



上面添加配置等于一个公共变量  任务中心可以通过 {{ name  }}  {{ git }} 获取到实际变量   属于是python 的tempalte模版是一种模版语法   还可以使用循环 判断 赋予 


主要的目的是

加配置各种加




通过配置内容变量 拼一个配置文件



写一个执行任务的脚本
如shell  ansible  ansibe-playbook 或者把拼出来的配置传给 你的服务 回调请求 


这样设计的目的是，灵活性，不需要懂python django的人 也可以对系统进行扩展功能





## 项目部署
## docker部署
## 本地部署




# 创建管理员账户密码
```bash
python3 manage.py  createsuperuser 


用户名 (leave blank to use 'mac-512'): huangchengwu
电子邮件地址: huangchengwu@163.com
Password: 
Password (again): 
密码跟 用户名 太相似了。
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```


# 表创建操作
python3 manage.py  makemigrations
python3 manage.py  migrate 
python3 manage.py runserver 0.0.0.0:9090


# 使用celery 原因

任务计划
任务调度
并行模型
io模型时间驱动



# 使用jenkins原因

拉代码
前端实时显示websocket代码
日志相关的存放
编写脚本，实时调试功能相关




jenkins缺点, 配置相关没有地方存 包括配置的组合虽然jenkins可以实现这些但是使用起来得你去适应它，定制化难

# haitun_cmdb
