from django.shortcuts import render
from django.http import HttpResponse
import datetime
import platform
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
# Create your views here.


def home(request):
    today=datetime.datetime.now().date()
    x = platform.system()
    # return render(request,'post/home.html', {"today1":today})
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, 'post/home.html', {"today" : today, "days_of_week" : daysOfWeek, "x":x})


def hello(request):
   return render(request, 'post/hello.html')


def register(request):
   return render(request, 'post/register.html')


# def sendSimpleEmail(request,emailto):
#    res = send_mail("hello paul", "comment tu vas?", "sirwin2win@gmail.com", [emailto], fail_silently=False)
#    return HttpResponse('%s'%res)

def sendSimpleEmail(request,emailto):
   w=send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
         ['sirwin2win@gmail.com'], fail_silently=False)
   return HttpResponse(w)


# posts/views.py
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'pics.html'


def see(request):
   contact=Contact.objects.all()
   context={'res':contact}
   return render(request, 'post/see.html', context)