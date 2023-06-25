# 基础镜像由python:3.10.9-alpine3.16打包成，替换成基础镜像后，后续打包上传会快一点只是更换层数和增加层数
# FROM  python:3.10.9-alpine3.16 
# WORKDIR  /haitun_cmdb
# COPY . /haitun_cmdb
# RUN  echo "https://mirrors.aliyun.com/alpine/v3.14/main" > /etc/apk/repositories && \
#     echo "https://mirrors.aliyun.com/alpine/v3.14/community" >> /etc/apk/repositories  && \  
#     apk update && apk add build-base dumb-init  && \
#     pip install --upgrade  pip -i https://mirrors.aliyun.com/pypi/simple/ && \
#     pip install -r requirements.txt  -i https://mirrors.aliyun.com/pypi/simple/ 
# ENTRYPOINT ["/usr/bin/dumb-init", "--"]
# CMD ["sh", "-c", "celery -A haitun_cmdb worker -l debug & python manage.py runserver 0.0.0.0:8000"]

#后续打包更换对应层就行 不需要重新搞一遍
FROM huangchengwu6904/hi-app:haitun_cmdb-base
COPY . /haitun_cmdb

