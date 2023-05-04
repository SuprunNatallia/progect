from django import forms
from app.models import Client
from app.models import Comment
from django.core.exceptions import ValidationError



class NewClientModelForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name', 'phone')

      
class NewCommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')

   
       


