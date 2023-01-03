from django.http import HttpResponse


# Create your views here.
def oauth(request):
    if request.method == "GET":
        return HttpResponse("oauth")
