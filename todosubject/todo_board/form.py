'''
from django import forms
from .models import Blog

class DataInput(forms.DataInput):
    input_type ='date'
class ToDoForms(forms.ModelForms):
    class Metak:
        model = Blog
        fields = ('title','end_data')
        widget = {'end_date':DataInput()}
        '''