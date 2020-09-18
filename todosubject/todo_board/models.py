from django.db import models


class Blog(models.Model):
   title = models.CharField(max_length=200)
   #dead_line = models.DateField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   body = models.TextField()
   def __str__(self):
       return self.title


  
# Create your models here.
