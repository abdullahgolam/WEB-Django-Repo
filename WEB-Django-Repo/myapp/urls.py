from django.urls import path
from myapp import views

urlpatterns = [
    # path('home/', views.home),
    # path('about/', views.about),
    # path('contact/', views.contact),
    # path('myip/', views.what_is_my_ip)

    path('', views.home)
]
