'''Views for placesmemo app'''
from django.shortcuts import render

def home(request):
    '''Home view'''
    template_name = 'home.html'
    return render(request, template_name)
