from django.db import models
from django.utils import timezone
from Doc.models import *

# Create your models here.


class Host(models.Model):
    # 主机名
    hostname = models.CharField(
        max_length=255, unique=True, verbose_name="主机名")
    # 内网 IP 地址
    internal_ip_address = models.GenericIPAddressField(
        unique=True, verbose_name="内网 IP 地址", null=True, blank=True)
    # 外网 IP 地址
    external_ip_address = models.GenericIPAddressField(
        unique=True, verbose_name="外网 IP 地址", null=True, blank=True)
    # SSH 用户名
    ssh_username = models.CharField(max_length=255, verbose_name="SSH 用户名")
    # SSH 密码
    ssh_password = models.CharField(max_length=255, verbose_name="SSH 密码")
    # 操作系统版本
    os_version = models.CharField(
        max_length=255, verbose_name="操作系统版本", null=True, blank=True)
    # 内核版本
    # kernel_version = models.CharField(max_length=255, verbose_name="内核版本")

    class Meta:
        verbose_name = "主机配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hostname


class cluster(models.Model):
    # 集群名字
    name = models.CharField(max_length=255, verbose_name="集群名字")
    kubeconfig = models.TextField(verbose_name="kubeconfig内容", default="")

    class Meta:
        verbose_name = "集群配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Custom(models.Model):
    # 集群名字
    name = models.CharField(max_length=255, verbose_name="配置名")
    config = models.TextField(verbose_name="配置内容", default="")

    class Meta:
        verbose_name = "自定义变量"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


env = """
#####env config
APP_NAME=HiCloud
APP_ENV=local
APP_KEY=base64:3b8bGAYz6khm9MTVA9MoRxXPElPs9P99bb37Z+A35Xc=
APP_DEBUG=false
APP_SCHEME=auto
APP_URL=https://hicloud.keli.vip
APP_DEV_URL=http://localhost:9998

"""
dockerfile = """
FROM  kuaifan/php:swoole-8.0.rc9
COPY ./co /var/www
"""


class k8sPm(models.Model):
    project_type_choices = [
        ("git", "git"),
        ("svn", "svn"),
    ]
    deoloy_status_choices = [
        ("未发布", "未发布"),
        ("发布中", "发布中"),

        ("已发布", "已发布"),


    ]

    name = models.CharField(
        max_length=255, verbose_name="项目名", default="cloud7")
    domain = models.CharField(
        max_length=255, verbose_name="部署域名", default="cloud7.keli.vip")

    Repositories = models.CharField(
        choices=project_type_choices, max_length=255, verbose_name="代码仓库类型", default=0)
    git = models.CharField(max_length=255, verbose_name="git地址",
                           default="https://github.com/innet8/cloud7.git")
    branch = models.CharField(
        max_length=255, verbose_name="分支", default="master")
    cmd = models.CharField(
        max_length=255, verbose_name="打包命令", default="bash -x cmd install")

    env = models.TextField(
        max_length=255, verbose_name="env", default=env)

    dockerfile = models.TextField(
        max_length=255, verbose_name="dockerfile", default=dockerfile)

    init = models.TextField(
        max_length=255, verbose_name="初始化命令", default="echo 'hello world'", null=True, blank=True)

    helm = models.CharField(
        max_length=255, verbose_name="helm", default="", null=True, blank=True)

    version = models.CharField(
        max_length=255, verbose_name="当前版本", default="", null=True, blank=True)

 
    deoloy_status = models.CharField(
        choices=deoloy_status_choices, max_length=255, verbose_name="发布状态", default=0)

    help = models.CharField(
        choices=deoloy_status_choices, max_length=255, verbose_name="发布状态", default=0)



    help = models.ForeignKey(HelpDocuments,  on_delete=models.CASCADE,verbose_name='帮助文档',related_name='pk_help',null=True)


    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    

    class Meta:
        verbose_name = "k8s项目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ecsPm(models.Model):
    project_type_choices = [
        ("git", "New"),
        ("svn", "svn"),
    ]

    name = models.CharField(
        max_length=255, verbose_name="项目名", default="cloud7")
    Repositories = models.CharField(
        choices=project_type_choices, max_length=255, verbose_name="代码仓库", default=0)
    git = models.CharField(max_length=255, verbose_name="git地址",
                           default="https://github.com/innet8/cloud7.git")
    branch = models.CharField(
        max_length=255, verbose_name="分支", default="master")
    cmd = models.CharField(
        max_length=255, verbose_name="打包命令", default="bash -x cmd install")
    package = models.CharField(
        max_length=255, verbose_name="打包工具版本", default="")

    class Meta:
        verbose_name = "ecs项目管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
