from django.http import HttpResponse
from django.shortcuts import render
from reminder.crawling.sadang import SaDang
from .task import test


# Create your views here.
def crawling(request):
    if request.method == 'GET':
        sadang = SaDang('사당중학교')
        sadang.crawling()
    return HttpResponse("test")
