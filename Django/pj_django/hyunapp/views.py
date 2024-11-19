from django.shortcuts import render
from django.http import  HttpResponse
from django.template import loader
from .models import Address

def index(request):
    template = loader.get_template('index.html')
    #return HttpResponse(template.render() #나중에 session 변수값을 받아오지 못함 
    return HttpResponse(template.render({},request)) #request 객체를 받으므로 확장성이 좋음 

def list(request):
    template = loader.get_template('list.html')
    addresses = Address.objects.all().values()
    context = {
        'addresses': addresses,
    }
    
    return HttpResponse(template.render(context,request))