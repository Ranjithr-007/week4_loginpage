from django.contrib import messages
from django.shortcuts import redirect,render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def login(reqeust):
    if reqeust.session.has_key('password'):
        return redirect(home)
    else:
        # if reqeust.method =='POST':
        #     uname = reqeust.POST['username']
        #     passwd = reqeust.POST['password']
        #     if uname == 'ranjith' and passwd == '1234':
        #         reqeust.session['password']=passwd
        #         return redirect(home)
        return render(reqeust, 'login.html')
        
def home(reqeust):
    if reqeust.session.has_key('password'):
        return render(reqeust, 'home.html')
    else:
        return redirect(login)
def send(request):
    if request.method =='POST':
        uname = request.POST['username']
        passwd = request.POST['password']
        if uname == 'ranjith' and passwd == '1234':
            request.session['password']=passwd
            return JsonResponse('true',safe=False)
        else:
            return JsonResponse('false',safe=False)
    
def logout(reqeust):
    if reqeust.session.has_key('password'):
        reqeust.session.flush()
        return redirect(login)
        