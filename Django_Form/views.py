from .forms import UsersForm
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    fn=UsersForm()              #Object Created
    data={'form':fn}            #data passed to template
    return render(request,"index.html",data)