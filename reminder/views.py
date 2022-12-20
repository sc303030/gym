from django.http import HttpResponse
from django.shortcuts import render
from .task import create_reminder_worker


# Create your views here.
def crawling(request):
    if request.method == 'GET':
        school_list = ['사당중학교', '봉은중학교']
        for school in school_list:
            create_reminder_worker.delay(school)
    return HttpResponse("test")
