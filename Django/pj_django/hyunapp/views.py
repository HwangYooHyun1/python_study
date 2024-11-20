from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Address, BoardAddress
from django.utils import timezone 
from django.urls import reverse ## 이전 페이지로 돌아가기 위해 import 

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

def write(request):
    template = loader.get_template('write.html')
    
    return HttpResponse(template.render({},request))

def write_ok(request):
    x = request.POST['name']
    y = request.POST['addr']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address = Address(name=x, addr=y, rdate=nowDatetime)
    address.save()
    # db저장 후 list로 돌아감
    return HttpResponseRedirect(reverse('list'))


def delete(request,id):
    address = Address.objects.get(id=id)
    address.delete()
    
    return HttpResponseRedirect(reverse('list'))
    
    
def update(request,id):
    template = loader.get_template('update.html')
    
    address = Address.objects.get(id=id)
    context = {
        'address': address,
    }
    return HttpResponse(template.render(context,request))

def update_ok(request, id):   #post방식으로 받아오는건 아래서 받아야함 
    x = request.POST['name']
    y = request.POST['addr']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    
    address = Address.objects.get(id=id)
    address.name = x
    address.addr = y
    address.rdate = nowDatetime
    address.save()
    
    return HttpResponseRedirect(reverse('list'))

def boardlist(request):
    template = loader.get_template('board/list.html')
    boardaddresses = BoardAddress.objects.all().values()
    context = { 'boardaddresses': boardaddresses}
    return HttpResponse(template.render(context, request ))

def board_write(request):
    template = loader.get_template('board/write.html')

    return HttpResponse(template.render({},request))

def board_write_ok(request):
    w = request.POST['writer']
    e = request.POST['email']
    s = request.POST['subject']
    c = request.POST['content']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

    boardaddress = BoardAddress(writer=w, email=e, subject=s, content=c, rdate=nowDatetime)
    boardaddress.save()

    return HttpResponseRedirect(reverse('boardlist'))

def board_content(request, id):
    template = loader.get_template('board/content.html')
    boardaddress = BoardAddress.objects.get(id=id)
    context ={'boardaddress' : boardaddress }
    return HttpResponse(template.render(context, request))

def board_update(request,id):
    template = loader.get_template('board/update.html')
    boardaddress = BoardAddress.objects.get(id=id)
    context = {'boardaddress':boardaddress}

    return HttpResponse(template.render(context, request))

def board_update_ok(request,id):
    w = request.POST['writer']
    e = request.POST['email']
    s = request.POST['subject']
    c = request.POST['content']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

    boardaddress = BoardAddress.objects.get(id=id)
    boardaddress.writer = w
    boardaddress.email = e
    boardaddress.subject = s
    boardaddress.content = c
    BoardAddress.rdate = nowDatetime
    boardaddress.save()

    return HttpResponseRedirect(reverse('boardlist'))

def board_delete(request, id):
    boardaddress = BoardAddress.objects.get(id=id)
    boardaddress.delete()
    
    return HttpResponseRedirect(reverse('boardlist'))