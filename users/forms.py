from django import forms
from .models import *

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)



  
class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = Hotel 
        fields = ['name', 'hotel_Main_Img'] 


class MakeDonation(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)



class ServForm(forms.ModelForm): 
  
    class Meta: 
        model = Serv 
        fields = ['name', 'username', 'code'] 

class EverForm(forms.ModelForm): 
  
    class Meta: 
        model = Ever 
        fields = ['name', 'username', 'code'] 


class TeachingForm(forms.ModelForm): 
  
    class Meta: 
        model = Teaching 
        widgets = {
        'password': forms.PasswordInput(),
        }
        fields = ['username','password', 'code']

class EvangelismForm(forms.ModelForm): 
  
    class Meta: 
        model = Evangelism 
        widgets = {
        'password': forms.PasswordInput(),
        }
        fields = ['username','password', 'code']

class StewardForm(forms.ModelForm): 
  
    class Meta: 
        model = Steward
        widgets = {
        'password': forms.PasswordInput(),
        } 
        fields = ['username','password', 'code']


class TesForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.PasswordInput()
    code = forms.CharField(max_length=50)


