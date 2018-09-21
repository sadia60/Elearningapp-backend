"""ElearningWebsit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Accounts.views import loginview,register_view,logout_view
from Dashboard.views import CourseList,CourseDetail,VideoList,VideoDetail
#from rango import views

#, register_view, logout_view)
from django.conf.urls import include, url
#from  import views

urlpatterns = [
    path('admin/', admin.site.urls),
#    path(r'^admin/',admin.site.urls),
    url(r'^course/', CourseList.as_view()),
    url(r'^courses/(?P<pk>[0-9]+)/$', CourseDetail.as_view()),

    url(r'^video/', VideoList.as_view()),
    url(r'^videos/(?P<pk>[0-9]+)/$', VideoDetail.as_view()),

    # url(r'^quiz/', QuizList.as_view()),
    #url(r'^quizs/(?P<pk>[0-9]+)/$', QuizDetail.as_view()),

    #    path(r'^login/', login_view, name='login'),
    url(r'^login/',loginview, name='login'),
    url(r'^register/', register_view, name='register'),

]
urlpatterns=format_suffix_patterns(urlpatterns)