from django.shortcuts import render,redirect

from django.views import View
from django.views import generic

class Todo_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        
        return render(request,'todo_main/index.html')

# Create your views here.
