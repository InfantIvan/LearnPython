from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! Hello world")

def faq(request):
    return HttpResponse("frequently asked questions")
