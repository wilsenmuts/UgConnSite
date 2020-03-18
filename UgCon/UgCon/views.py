from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django_chatter.views import ChatRoomView
from django_chatter.utils import create_room
from flashcards.models import User

def home1(request):
    return HttpResponse("The response")


def success(request):
    return HttpResponse('The operation was a success.')


def failure(request):
    return HttpResponse('ERROR!!!!  Failed to complete operation. Retry. In case, it persists, report to developer or administrator.')



def home(request):
    '''
    Render the request for home.html
    '''
    if request.method == 'POST':
        username_input = request.POST.get('uname', None)
        password_input = request.POST.get('pword', None)
        user = authenticate(username=username_input, password=password_input)
        if user is not None:
            request.session['username'] = username_input
            login(request, user)
            return HttpResponseRedirect('flashcards/activity')
        else:
            return HttpResponse('Check your details and retry to login')
    context = {} #an empty dictionary
    return render(request, 'home.html', context)

def log_out(request):
    del request.session['username']
    logout(request)
    return HttpResponse("<strong>You are logged out.</strong>")

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
        return HttpResponse('You have been successfully registered...')
    context = {}
    return render(request, 'register.html', context=None)


def my_view(request):
    user1 = request.user # User requesting the view
    user2 = User.objects.get(username="user2") # example user in your db
    room_id = create_room([user1, user2])
    return ChatRoomView(request, room_id)