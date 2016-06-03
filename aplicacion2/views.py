from django.shortcuts import render

# Create your views here.
from aplicacion2.forms import Login


def login (request):
    context= dict()
    form= Login()

    context['form']=form

    return render(request,template_name='login.html',context=context)
