'''This is the views.py file for the places app'''
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    '''This is the index view for the places app.'''
    return HttpResponse("Hello, world. You're at the polls index.")
