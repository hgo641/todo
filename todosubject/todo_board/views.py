from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from django.views import View
from django.views import generic

'''	
def home(request):
    blogs = Blog.objects
    return render(request, 'todo_board/todo_list.html', {'blogs' : blogs})
'''

class Todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        return render(request,'todo_board/todo_list.html', {'blogs' : blogs})
def home(request):
    blogs = Blog.objects
    return render(request, 'todo_board/todo_list.html', {'blogs' : blogs})

def postnew(request):
    return render(request, 'todo_board/postnew.html')

def postcreate(request):
    print(request.method)
    if(request.method == 'POST'):
      #<form action="{% url 'postcreate' %}" method="post">
      #hello/templates/postnew.html 파일 메서드 확인
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    return redirect('todo_board')

def detail(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render(request,'todo_board/detail.html',{'onepost':onepost})

def postedit(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render(request,'todo_board/postedit.html',{'onepost':onepost})

def postupdate(request,post_id):
    editpost=get_object_or_404(Blog,pk=post_id)
    editpost.title=request.POST['title']
    editpost.body=request.POST['body']
    editpost.save()
    return redirect('/detail/'+str(post_id))

def postdelete(request,post_id):
    deletepost=get_object_or_404(Blog,pk=post_id)
    deletepost.delete()
    return redirect('todo_board')


