version ?= 1
migrate:
	python3 manage.py  makemigrations
	python3 manage.py  migrate 
build:
	
	docker build -t  docker.io/huangchengwu6904/hi-app:haitun_cmdb-v${version}  .
	docker push docker.io/huangchengwu6904/hi-app:haitun_cmdb-v${version}

celery:
	celery  -A haitun_cmdb worker  -l debug -P eventlet
run:
	python3 manage.py runserver  
