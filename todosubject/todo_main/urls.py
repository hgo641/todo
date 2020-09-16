from django.conf.urls import include,url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = 'todo_main'

urlpatterns = [
    path(r'^$', views.todo_main.as_view(),name='todo_main'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)