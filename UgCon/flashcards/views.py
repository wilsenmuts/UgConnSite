from django.shortcuts import render, get_object_or_404, redirect
from django.http  import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
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

def activity(request):
    '''
    renders the flashcards activity page
    '''
    return render(request, 'flashcards/activity.html', context=None)



def analysis(request):
    '''
    The flashcards analytics page
    '''
    return render(request, 'flashcards/analysis.html', context=None)



def apk_download(request):
    return HttpResponse('<p style="color:darkred;font-size:1.2em">Sorry!!! File is being built for you and will be available as soon as possible.</p>')



def apps(request):
    '''
    renders the page tos show off applications.
    '''
    return render(request, 'flashcards/apps.html', context=None)


def buyequipment(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = buyitem(
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
            reply='Your Request was sent to UgCon successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, "flashcards/buyequipment.html", context)


def buyhouse1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = buyhouse(
                username = myusername,
                reside = request.POST.get('org'),
                structure = request.POST.get('type'),
                description = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to UgCon successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, "flashcards/buyhouse.html", context)


def buyland1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = buyland(
                username = myusername,
                reside = request.POST.get('org'),
                structure = request.POST.get('type'),
                notes = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to UgCon successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, "flashcards/buyland.html", context)


def buildhouse1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = buildhouse(
                username = myusername,
                reside = request.POST.get('org'),
                structure = request.POST.get('type'),
                serviceprovider = request.POST.get('provider'),
                brief = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to UgCon successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, "flashcards/buildhouse.html", context)


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
    renders contact to the UgConn team
    '''
    return render(request, 'flashcards/contactugc.html', context=None)


def donatemoney1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = donatemoney(
                username = myusername,
                orgname = request.POST.get('org'),
                activity = request.POST.get('type'),
                reside = request.POST.get('reside'),
                contact = request.POST.get('contact'),
                notes = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to UgCon successfully!'
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



def home(request):
    '''
    renders the flashcards home page
    '''
    qry= get_object_or_404(about, title='UgCon')
    context={'about':qry}

    return render(request,'flashcards/home.html',context)


def investmoney1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = investmoney(
                username = myusername,
                title = request.POST.get('title'),
                activity = request.POST.get('activity'),
                notes = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to UgCon successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, "flashcards/investmoney.html", context)


def myactivity(request):
    '''
    renders the my activity page
    '''
    if request.method =='GET':
        sword= request.GET.get('type')
        print(sword)
    return render(request, 'flashcards/myactivity.html', context=None)



def myaccount(request):
    '''
    renders my account page
    '''
    return render(request, 'flashcards/myaccount.html', context=None)



def others1(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = others(
                username = myusername,
                activity = request.POST.get('activity'),
                notes = request.POST.get('notes',)
            )
            buy_equip.save()
            reply='Your Request was sent to UgCon successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, 'flashcards/others.html', context)



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


def payment(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            buy_equip = feesandbills(
                username = myusername,
                activity = request.POST.get('type'),
                amount = request.POST.get('amount'),
                payplan = request.POST.get('payplan'),
                receiver = request.POST.get('receiver'),
                notes = request.POST.get('notes'),
            )
            buy_equip.save()
            reply='Your Request was sent to UgCon successfully!'
            context={'reply':reply}
            return render(request, "flashcards/activity.html", context)

        return redirect('/')
    context={}
    return render(request, 'flashcards/pay.html', context)


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


def siteservices(request):
    site_services = service.objects.order_by('title')
    context={'site_services':site_services}
    return render(request, 'flashcards/siteservices.html', context)


def sought(request, src_id):
    print(src_id)
