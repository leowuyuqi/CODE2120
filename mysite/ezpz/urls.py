from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path(r'ezpz_get/<str:var_a>/<str:var_b>',  views.ezpz_get),
	path(r'caculate/', views.caculate),
]