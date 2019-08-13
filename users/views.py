from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import reportlab
from django.contrib.auth import authenticate, login
from .forms import ContactForm, MakeDonation
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
# from hubspot.signals import payment_verified

from django.dispatch import receiver
# Create your views here.


def register(request):
    if request.method=='POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           username=form.cleaned_data.get('username')
           messages.success(request, f'Account created for {username}!')
           return redirect('post-home')
    else:
        form=UserCreationForm()
    return render(request, "users/register.html", {'form': form})


# def email(request):
#     subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['sirwin2win@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('post-home')



from reportlab.pdfgen import canvas
from django.http import HttpResponse

def pics(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'    
    filename="somefilename.pdf"

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response 


def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['sirwin2win@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('successView')
    return render(request, "users/email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')




def img(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('photo') 
    else: 
        form = HotelForm() 
    return render(request, 'users/img.html', {'form' : form})



def photo(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Hotels = Hotel.objects.all()  
        return render(request, 'users/photo.html', {'hotel_images' : Hotels})

def pay(request): 
  
    if request.method == 'POST': 
        form = MakeDonation(request.POST) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('photo') 
    else: 
        form = MakeDonation() 
    return render(request, 'users/pay.html', {'form' : form})


# @receiver(payment_verified)
# def on_payment_verified(sender, ref,amount, **kwargs):
#     """
#     ref: paystack reference sent back.
#     amount: amount in Naira.
#     """
#     pass


# def regi(request):
#     res=register.objects.all()



def serv1(request): 
  
    if request.method == 'POST': 
        form = ServForm(request.POST) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('photo') 
    else: 
        form = ServForm() 
    return render(request, 'users/serv1.html', {'form' : form})



def ev(request): 
  
    if request.method == 'POST': 
        form = EverForm(request.POST) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('photo') 
    else: 
        form = EverForm() 
    return render(request, 'users/ev.html', {'form' : form})

def teaching(request): 
  
    if request.method == 'POST': 
        form = TeachingForm(request.POST) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('photo') 
    else: 
        form = TeachingForm() 
    return render(request, 'users/teaching.html', {'form' : form})


def evangelism(request): 
  
    if request.method == 'POST': 
        form = EvangelismForm(request.POST) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('photo') 
    else: 
        form = EvangelismForm() 
    return render(request, 'users/evangelism.html', {'form' : form})

def steward(request): 
  
    if request.method == 'POST': 
        form = StewardForm(request.POST) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('photo') 
    else: 
        form = StewardForm() 
    return render(request, 'users/steward.html', {'form' : form})



def tes(request):
    form_class = TesForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # code = request.POST.get('code')
        # form=TesForm(request.POST)
        username = request.POST['username']
        code = request.POST['code']
        user = authenticate(username=username, code=code)
        # user = authenticate(username=username, password=password, code=code)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('photo')
            elif user.is_active and code==222:
                login(request,user)
                return redirect('post-home')
            elif user.is_active and code==333:
                login(request,user)
                return redirect('post-about')
    return render(request, 'users/tes.html', {'form' : form})


                      