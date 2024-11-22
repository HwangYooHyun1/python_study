from django.shortcuts import render, redirect
from django.http import  HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Address, BoardAddress, Member
from django.utils import timezone 
from django.urls import reverse ## 이전 페이지로 돌아가기 위해 import 
from django.db.models import Q ##filter 여러 or 문 처리 

def index(request):
    template = loader.get_template('index.html')
    #return HttpResponse(template.render() #나중에 session 변수값을 받아오지 못함 
    return HttpResponse(template.render({},request)) #request 객체를 받으므로 확장성이 좋음 

def list(request):
    template = loader.get_template('list.html')
    #addresses = Address.objects.all().values()  #모든 데이터 출력
    #addresses = Address.objects.filter(name='홍길동').values() #원하는 데이터 필터링
    #addresses = Address.objects.filter(name='홍길동',addr='서울').values() # where ... and 조건
    #addresses = Address.objects.filter(name='홍길동').values() | Address.objects.filter(addr='부산').values() # where ... or 조건 
    #addresses = Address.objects.filter(Q(name='홍길동')|Q(addr='부산')).values() #or문을 간략하게
    #addresses = Address.objects.filter(name__startswith='이').values() #column name 뒤에 __를 붙히고 옵션을 붙힘 
    #addresses = Address.objects.all().order_by('-name').values() #내림차순 정렬 (- = desc)
    addresses = Address.objects.all().order_by('-name','addr','-id').values() #여러 조건으로 정렬
    
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

def login(request):
    #template = loader.get_template('login.html')
    #return HttpResponse(template.render({},request))
    return render(request, 'login.html')  #다른 방법 

def login_ok(request): 
    email = request.POST['email']
    pwd = request.POST['pwd']
    
    #로그인 정보 비교 
    try:
        member = Member.objects.get(email=email)
    except Member.DoesNotExist:
        member = None
    
    result = 0
    if member!= None:
        print('해당 회원이 존재')
        if member.pwd == pwd:
            print('비밀번호 일치')
            result =2
            #request를 통한 session 접근 가능 
            #서버층 세션 메모리방에 key,value dict 형태로 저장
            request.session['login_ok_user']  = member.email 
        else:
            print('비밀번호 불일치')
            result = 1
    else:
        print('해당 회원이 존재하지 않음')
        result = 0
       
    template = loader.get_template('login_ok.html')
    context = {
        'result': result, #2:success, 1:pwd error 0:email non-exist
    }
    return HttpResponse(template.render(context,request))

def logout(request):
    if request.session.get('login_ok_user'):
        del request.session['login_ok_user']

    #redirect는 새로운 경로를 요청하는 것, url 자체가 바뀜(새로고침) --> session에 저장된 data가 사라져야하니까!
    return redirect("../") 

#board 
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

#template

def test1(request):
    addresses = Address.objects.all().values()
    template = loader.get_template("template1.html")
    context = {
        'yourname':'길동',
        'addresses': addresses
    }
    return HttpResponse(template.render(context, request))

def test2(request):
    template = loader.get_template("template2.html")
    context = {
        'x': 2,
        'y': 'tiger',
        'fruits': ['apple', 'orange'],
        'fruits2': ['apple', 'orange'],
    }
    return HttpResponse(template.render(context, request))

def test3(request):
    addresses = Address.objects.all().values()
    temlate = loader.get_template("template3.html")
    context = {
        'fruits': ['apple', 'orange', 'melon'],
        'cars': [{'brand':'현대', 'model':'소나타', 'year':'2022'}, {'brand':'테슬라', 'model':'모델X', 'year':'2020'}],
        #'addresses': addresses,
    }
    return HttpResponse(temlate.render(context, request))

def test4(request):
    temlate = loader.get_template("template4.html")
    context = {
        'name': '홍길동',
    }
    return HttpResponse(temlate.render(context, request))

def test5(request):
    addresses = Address.objects.all().values()
    temlate = loader.get_template("template5.html")
    context = {
        'addresses': addresses,
    }
    return HttpResponse(temlate.render(context, request))

def test6(request):
    addresses = Address.objects.all().values()
    temlate = loader.get_template("template6.html")
    context = {
        'addresses': addresses,
    }
    return HttpResponse(temlate.render(context, request))

def test7(request):
    temlate = loader.get_template("template7.html")
    context = {}
    return HttpResponse(temlate.render(context, request))

def test8(request):
    temlate = loader.get_template("template8.html")
    context = {}
    return HttpResponse(temlate.render(context, request))