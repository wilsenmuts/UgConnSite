from django.shortcuts import render, get_object_or_404, redirect
from django.http  import HttpResponse, HttpResponseRedirect
from .models import *
from adminApp.models import *
from .forms import *
from itertools import chain
from django.core.paginator import Paginator
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout


#*************************************************************************************************************Notification
def success(request):
    return HttpResponse('The operation was a success.')

def failure(request):
    return HttpResponse('ERROR!!!!  Failed to complete operation. Retry. In case, it persists, report to developer or administrator.')

#*************************************************************************************************************** Create your views here.

@login_required(login_url="/")
def activity(request):
    '''
    renders the flashcards activity page
    '''
    partners = partner.objects.all()
    return render(request, 'flashcards/activity.html', context={"partners":partners})

@login_required(login_url="/")
def analysis(request):
    '''
    The flashcards analytics page
    '''
    return render(request, 'flashcards/analysis.html', context=None)

def apk_download(request):
    context={}
    return render(request,"flashcards/comingSoon.html", context)

def apps(request):
    '''
    renders the page tos show off applications.
    '''
    return render(request, 'flashcards/apps.html', context=None)

@login_required(login_url="/")
def show_notes(request):
    context={}
    return render(request,"flashcards/notes.html", context)

@login_required(login_url="/")
def buyequipment(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = buyitem(
                name= request.POST.get('project_name'),
                username = myusername,
                item = request.POST.get('item'),
                quantity = request.POST.get('quantity'),
                quality = request.POST.get('quality'),
                receiver = request.POST.get('target_p'),
                contact = request.POST.get('contact'),
                reside = request.POST.get('target_l'),
                notes = request.POST.get('notes'),

            )
            buy_equip.save()
            reply='Your Request was sent to Reconna successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, "flashcards/buyequipment.html", context)

@login_required(login_url="/")
def buyhouse1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = buyhouse(
                name= request.POST.get('project_name'),
                username = myusername,
                reside = request.POST.get('org'),
                structure = request.POST.get('type'),
                notes = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to Reconna successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, "flashcards/buyhouse.html", context)

@login_required(login_url="/")
def buyland1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = buyland(
                name = request.POST.get('project_name'),
                username = myusername,
                reside = request.POST.get('org'),
                structure = request.POST.get('type'),
                notes = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to Reconna successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, "flashcards/buyland.html", context)

@login_required(login_url="/")
def buildhouse1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = buildhouse(
                name=request.POST.get('project_name'),
                username = myusername,
                reside = request.POST.get('org'),
                structure = request.POST.get('type'),
                serviceprovider = request.POST.get('provider'),
                notes = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to Reconna successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, "flashcards/buildhouse.html", context)

@login_required(login_url="/")
def createDeck(request):
    '''
    create Deck
    '''
    if request.method == 'POST':
        fname_input = request.POST.get('fname', None)
        sname_input = request.POST.get('sname', None)
        uname_input = request.POST.get('uname', None)
        email_input = request.POST.get('email', None)
        pswd_input = request.POST.get('pswd', None)
        print(request.POST)
        create_user = users(
            firstname=fname_input,
            surname=sname_input,
            username= uname_input,
            email= email_input,
            password=pswd_input
            )
        create_user.save()
        return HttpResponseRedirect('/flashcards')
    context = {}
    return render(request, 'flashcards/createDeck.html', context)

@login_required(login_url="/")
def connect(request):
    '''
    renders the flashcards connection module
    '''
    room_name= request.session.has_key('username')
    context={'room_name':room_name}
    return render(request, 'flashcards/connect.html', context)

def contactdev(request):
    '''
    renders the page for contacting the developers of the system
    '''
    return render(request, 'flashcards/contactdev.html', context=None)

def contactugc(request):
    '''
    renders contact to the Reconna team
    '''
    return render(request, 'flashcards/contactugc.html', context=None)

@login_required(login_url="/")
def donatemoney1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = donatemoney(
                name=request.POST.get('project_name'),
                username = myusername,
                orgname = request.POST.get('org'),
                activity = request.POST.get('type'),
                reside = request.POST.get('reside'),
                contact = request.POST.get('contact'),
                notes = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to Reconna successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, "flashcards/donatemoney.html", context)

#def editdeck(request, article_id):
    '''
    edit information about deck
    '''
   # article_obj = get_object_or_404(article, id=article_id)
    #if request.method =='POST':
    #    form = UgBuSForm(request.POST, instance=article_obj)
    #    add_activity= article(
    #        title = request.POST.get('title'),
    #        date_as_is = datetime.now(),
    #        about = request.POST.get('options'),
    #        notes = request.POST.get('message')
    #    )
    #    add_activity.save()
    #    print (request.POST)
    #    if form.is_valid():
    #       return HttpResponse('Posted')
    #else:
    #    form = UgBuSForm(article_obj)
    #context = {'form':form}
    #return render(request, 'flashcards/UgBus.html', context)
@login_required(login_url="/")
def grievances(request):
    '''
    renders the page to enable grievances
    '''
    if request.method=='POST':
        title_grieve = request.POST.get('title', None)
        about_grieve = request.POST.get('about', None)
        describe_grieve = request.POST.get('description', None)
        print(request.POST)
        new_grieve = grieve(
            title=title_grieve,
            about = about_grieve,
            notes = describe_grieve
        )
        new_grieve.save()
        return HttpResponse('Success!')
    context={}
    return render(request, 'flashcards/grievances.html', context)

@login_required(login_url="/")
def home(request):
    '''
    renders the flashcards home page
    '''
    qry= get_object_or_404(about, title='Reconna')
    context={'about':qry}

    return render(request,'flashcards/home.html',context)

@login_required(login_url="/")
def investmoney1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = investmoney(
                name = request.POST.get('project_name'),
                username = myusername,
                title = request.POST.get('title'),
                activity = request.POST.get('activity'),
                notes = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to Reconna successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, "flashcards/investmoney.html", context)

@login_required(login_url="/")
def myactivity(request):
    '''
    renders the my activity page
    '''
    OtherActivities = others.objects.filter(username=request.user).order_by('name')
    PayFess = feesandbills.objects.filter(username=request.user).order_by('name')
    BuyLand = buyland.objects.filter(username=request.user).order_by('name')
    BuyHouse_list= buyhouse.objects.filter(username=request.user).order_by('name')
    BuyEquipment = buyitem.objects.filter(username=request.user).order_by('name')
    DonateMoney = donatemoney.objects.filter(username=request.user).order_by('name')
    InvestMoney= investmoney.objects.filter(username=request.user).order_by('name')
    Buildhouse= buildhouse.objects.filter(username=request.user).order_by('name')
    print(BuyHouse_list)
    result_list = list(chain(InvestMoney, Buildhouse, DonateMoney, BuyEquipment, BuyHouse_list, BuyLand, PayFess, OtherActivities))
    context={"projects":result_list}
    return render(request, 'flashcards/myactivity.html', context)

@login_required(login_url="/")
def myaccount(request):
    '''
    renders my account page
    '''
    return render(request, 'flashcards/myaccount.html', context=None)

@login_required(login_url="/")
def others1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = others(
                name= request.POST.get('project_name'),
                username = myusername,
                activity = request.POST.get('activity'),
                notes = request.POST.get('notes',)
            )
            buy_equip.save()
            reply='Your Request was sent to Reconna successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, 'flashcards/others.html', context)

@login_required(login_url="/")
def popDeck(request):
    '''
    populate model form
    '''
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= UserForm
    context = {'form':form}
    return render(request, 'flashcards/createDeck.html', context)

@login_required(login_url="/")
def payment(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = feesandbills(
                name=request.POST.get('project_name'),
                receiver_contact = request.POST.get('contact'),
                username = myusername,
                activity = request.POST.get('type'),
                amount = request.POST.get('amount'),
                payplan = request.POST.get('payplan'),
                receiver = request.POST.get('receiver'),
                notes = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to Reconna successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, 'flashcards/pay.html', context)

@login_required(login_url="/")
def ugbus(request):
    '''
    renders the flashcards ugbusiness page
    '''
    if request.method =='POST':
        form = UgBuSForm(request.POST)
        add_activity= article(
            title = request.POST.get('title'),
            date_as_is = datetime.now(),
            about = request.POST.get('options'),
            notes = request.POST.get('message')
        )
        add_activity.save()
        print (request.POST)
        if form.is_valid():
           return HttpResponse('Posted')
    else:
        form = UgBuSForm()
    qry= article.objects.order_by('-date_as_is')
    paginator = Paginator(qry, 8) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'form':form,'my':page_obj}
    return render(request, 'flashcards/UgBus.html', context)

@login_required(login_url="/")
def siteservices(request):
    site_services = service.objects.order_by('title')
    context={'site_services':site_services}
    return render(request, 'flashcards/siteservices.html', context)

@login_required(login_url="/")
def sought(request, src_id):
    print(src_id)
