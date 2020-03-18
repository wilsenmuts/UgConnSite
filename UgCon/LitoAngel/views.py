from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import litoangel

# Create your views here.
def home(request):
    if request.method == 'POST':
        room_name = request.POST.get('msg')
        return redirect('/Litoangel/chat/%s' % room_name)
    context={}
    return render(request, 'litoangel/index.html', context)


def success(request):
    return HttpResponse('The operation was a success.')


def failure(request):
    return HttpResponse('ERROR!!!!  Failed to complete operation. Retry. In case, it persists, report to developer or administrator.')

def room(request, room_name):
    context={'room_name': room_name}
    return render(request, 'chat/room.html', context)


class HomeView(ListView):
    model = litoangel
    template_name = 'litoangel/index.html'

