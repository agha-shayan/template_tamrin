from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def salam(request):
    return HttpResponse("s")
def index_page(request):
    return render(request,'index.html')