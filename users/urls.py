from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.checks import register

from . import views

urlpatterns=[
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    url(r'^logout/$',views.logout_view,name='logout_view'),
    url(r'^register/$',views.register,name='register'),
]
