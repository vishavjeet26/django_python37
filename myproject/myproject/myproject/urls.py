"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from myapp import views

urlpatterns = [
   #path('myapp/', include('myapp.urls')),
   path('admin/', admin.site.urls),
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('test/<int:id>', views.test, name='test'),
    path('testValue/<str:value>', views.testValue, name='testValue'),

    path('hello/', views.hello, name='hello'),
    path('helloHtml/', views.helloHtml, name='helloHtml'),
    path('current_datetime/', views.current_datetime, name='current_datetime'),
    path('current_datetime2/', views.current_datetime2, name='cd'),
    path('template/', views.template, name='template'),
   # path('readTemplate/', views.readTemplate, name='readTemplate'),
   path('includeTemplate/', views.includeTemplate, name='includeTemplate'),
   path('book_list/', views.book_list, name='book_list'),
   path('crudops/', views.crudops, name='crudops'),
   path('datamanipulation/', views.datamanipulation, name='datamanipulation'),
   path('linkingModel', views.linkingModel, name='linkingModel'),

]








