from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse
import os
import platform
from datetime import datetime

# function based-view

# def what_is_my_ip(request):
#     return JsonResponse({'ip':'192.133.125.99'})

# def home(request):  #www.example.com/home
    # return HttpResponse('<h1>Hello From Home!</h1>')
    # return FileResponse(open('myapp/media/example.jpg', 'rb'))
    # return FileResponse(open('myapp/media/example.mp3', 'rb'))
    # return FileResponse(open('myapp/media/example.mp4', 'rb'))

# def about(request):  #www.example.com/about
#     return HttpResponse('<h1>Hello From About!</h1>')

# def contact(request):  #www.example.com/contact
#     return HttpResponse('<h1>Hello From Contact!</h1>')

def home(request):
    return render(request=request, 
                    template_name='index.html', 
                    context={'name':'Abdullah',
                                'age': 31,
                                'dir':os.getcwd(),
                                'ptf': platform.platform,
                                'myname': '',
                                'filesize': 12534596557423,
                                'addnum':5,
                                'capfirst':"hello",
                                'cuttext':'hello hello hello',
                                'datetime': datetime.now,
                                'floting': 7.900009,
                                'upeertext': 'ABDULLAH GOLAM',
                                'lowertext': 'abdullah golam',
                                'randomnumber': [1, 2, 3, 9, 10, 23, 13],
                                # we can use slice with list
                                'sliceany': 'abdullah golam',
                                'slugifyany': 'abdullah golam'})

# def home(request):
#     return render(request, 'index.html')