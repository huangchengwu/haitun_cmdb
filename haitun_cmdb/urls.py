"""
URL configuration for haitun_cmdb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken.views import obtain_auth_token


from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls import include,url

schema_view = get_schema_view(
    openapi.Info(
        title="海豚有海运维系统 API",  # 名称
        default_version="版本 v1.0.0",  # 版本
        description="海豚有海运维系统API文档",  # 项目描述
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ConfCen/", include("ConfCen.urls")),
    path("Doc/", include("Doc.urls")),

    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),


    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),

    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path("api-token-auth/", obtain_jwt_token),
    url(r"^uploads/(?P<path>.*)", serve,
        {"document_root": settings.MEDIA_ROOT}),
    url('', include('django_prometheus.urls')),


]






