from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib import messages
from .token import acc_token
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .forms import Register
from .models import Movie,New, Account
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
# Create your views here.

def log(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= authenticate(username=username, password=password)

        print(username,password)

        if user is not None:
            login(request,user)
            return redirect ('home')
        
        else:
            messages.error(request,'INVALID USERNAME OR PASSWORD')
            return redirect('log')
    
    else:
        return render( request, 'login.html')

def sign(request):
    if request.method == 'POST':
        form = Register(request.POST)

        if form.is_valid():
            user= form.save(commit=False)
            user.is_active= False
            user.save()

            current_site=get_current_site(request)
            mail_subject= 'Activation Link has been sent to your email'

            message= render_to_string('email.html' , {
                'user' :user,
                'domain' : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : acc_token.make_token(user)
            })

            to_email= form.cleaned_data.get('email')
            email= EmailMessage(mail_subject,message,to=[to_email])
            email.send()

            messages.success(request,'💌 A Link has been sent to your Email. CLick it to Complete Registration ')
            return redirect('sign')

    else:
        form = Register()
    return render( request, 'sign.html', {'form' : form})

def activate(request, uidb64, token):
    User= get_user_model()

    try:
        uid= force_str(urlsafe_base64_decode(uidb64))
        user= Account.objects.get(pk=uid)

    except {TypeError, ValueError, OverflowError, Account.DoesNotExist}:
        user = None
    
    if user is not None and acc_token.check_token(user, token):
        user.is_active= True
        user.save()

        return redirect('log')
    else:
        return HttpResponse('Activation Link Invalid')

def home(request):
    movies= Movie.objects.all()
    new= New.objects.all()

    paginator= Paginator(movies,4)

    page= request.GET.get('page')

    try:
        m= paginator.page(page)
    except PageNotAnInteger:
        m= paginator.page(1)
    except EmptyPage:
        m= paginator.page(paginator.num_pages)

    searchtitle= request.GET.get('movie')

    if searchtitle:
        api_key = '26a6d4eb'
        movie_data= getmovie(searchtitle,api_key)

        return render(request,'home.html' , {'m':m, 'new':new, 'movie_data' : movie_data})
    
    return render(request, 'home.html', {'m':m, 'new':new})

def getmovie(moviet,api_key):
    url= f'http://www.omdbapi.com/?t={moviet}&apikey={api_key}'
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        return data

    else:
        return None

def logout_user(request):
    logout(request)
    return redirect('log')