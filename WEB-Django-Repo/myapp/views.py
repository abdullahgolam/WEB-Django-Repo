from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse

# function based-view

def what_is_my_ip(request):
    return JsonResponse({'ip':'192.133.125.99'})

def home(request):  #www.example.com/home
    return HttpResponse('<h1>Hello From Home!</h1>')
    # return FileResponse(open('myapp/media/example.jpg', 'rb'))
    # return FileResponse(open('myapp/media/example.mp3', 'rb'))
    # return FileResponse(open('myapp/media/example.mp4', 'rb'))

def about(request):  #www.example.com/about
    return HttpResponse('<h1>Hello From About!</h1>')

def contact(request):  #www.example.com/contact
    return HttpResponse('<h1>Hello From Contact!</h1>')