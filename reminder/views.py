from django.http import HttpResponse
from django.shortcuts import render
from reminder.crawling import sadang


# Create your views here.
def crawling(request):
    if request.method == 'GET':
        print(sadang())
    return HttpResponse("test")