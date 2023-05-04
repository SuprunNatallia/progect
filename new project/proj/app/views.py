from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Massages, Cosmetolog, Specialists, Comment
from app.forms import forms



def price (request):
    massage = Massages.objects.all().values()
    cosmetology = Cosmetolog.objects.all().values()
    template = loader.get_template('price.html')
    context = {'massage':massage, 'cosmetology':cosmetology}
    return HttpResponse(template.render(context,request))



def home (request):
    if request.method == "POST":
        form = forms.NewClientModelForm(request.POST, request.FILES)
        if form.is_valid():
            client_entry = form.save(commit=False)
            client_entry.save()
            form.save_m2m()
            return redirect('thanks')
    else:
        form = forms.NewClientModelForm()
    return render(request, 'home.html', {'form':form})


def reviews (request):
    if request.method == "POST":
        form = forms.NewCommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment_entry = form.save(commit=False)
            comment_entry.issued =  datetime.datetime.now()
            comment_entry.save()
            form.save_m2m()
            return HttpResponseRedirect(request.path_info) 
    else:
        form = forms.NewCommentModelForm()
        comments = Comment.objects.all().order_by('-issued').values()
    return render(request, 'reviews.html', {'form':form, 'comments':comments})


def specialists (request):
    specialists = Specialists.objects.all()
    return render(request, 'specialists.html', {'specialists':specialists})

def about (request):
    return render(request, 'about.html')

def thanks (request):
    return render(request, 'thanks.html')