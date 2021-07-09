from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from adminApp.models import *
@login_required(login_url="/")
def home1(request):
    return HttpResponse("The response")

@login_required(login_url="/")
def success(request):
    return HttpResponse('The operation was a success.')

@login_required(login_url="/")
def failure(request):
    return HttpResponse('ERROR!!!!  Failed to complete operation. Retry. In case, it persists, report to developer or administrator.')


def show_index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/flashcards/activity')
    else:
        partners = partner.objects.all()
        context = {'partners':partners}
        return render(request, "index.html", context)

def home(request):
    '''
    Render the request for home.html
    '''
    if request.user.is_authenticated:
        return HttpResponseRedirect('/flashcards/myactivity')
    else:
        if request.method == 'POST':
            username_input = request.POST.get('uname', None)
            password_input = request.POST.get('pword', None)
            user = authenticate(username=username_input, password=password_input)
            if user is not None:
                request.session['username'] = username_input
                login(request, user)
                return HttpResponseRedirect('/flashcards/activity')
            else:
                context={'query':'Invalid login details. Please try again or register...'}
                return render(request, 'home.html', context)
        partners = partner.objects.all()
        context = {'partners':partners}
        return render(request, 'index.html', context)

def show_index(request):
    if request.method == 'POST':
        username_input = request.POST.get('uname', None)
        password_input = request.POST.get('pword', None)
        user = authenticate(username=username_input, password=password_input)
        if user is not None:
            request.session['username'] = username_input
            login(request, user)
            return HttpResponseRedirect('/flashcards/activity')
        else:
            context={'query':'Invalid login details. Please try again or register...'}
            return render(request, 'home.html', context)
    context = {} #an empty dictionary
    return render(request, 'home.html', context)

def log_out(request):
    #del request.session['username']
    logout(request)
    return HttpResponseRedirect("/")

def register(request):
    '''
    renders registration page
    '''
    if request.method == 'POST':
        fname_input = request.POST.get('fname', None)
        sname_input = request.POST.get('sname', None)
        uname_input = request.POST.get('uname', None)
        email_input = request.POST.get('email', None)
        pswd_input = request.POST.get('pswd', None)
        user = User.objects.create_user(
            first_name = fname_input,
            last_name = sname_input,
            username = uname_input,
            email = email_input,
            password = pswd_input,


        )
        return HttpResponseRedirect('/flashcards/activity')
    context = {}
    return render(request, 'register.html', context=None)