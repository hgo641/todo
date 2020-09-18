"""todosubject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include, url
import todo_board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todo_main.urls')),
    path('board/',todo_board.views.Todo_board.as_view(), name = 'todo_board'),
    path('new/',todo_board.views.postnew, name = 'postnew'),
    path('create/',todo_board.views.postcreate, name='postcreate'),
    path('detail/<int:post_id>',todo_board.views.detail,name="detail"),
    path('edit/<int:post_id>',todo_board.views.postedit,name="postedit"),
    path('postupdate/<int:post_id>',todo_board.views.postupdate,name="postupdate"),
    path('postdelete/<int:post_id>',todo_board.views.postdelete,name="postdelete"),
]
