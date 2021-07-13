from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import *
from flashcards.models import *
from django.contrib.auth.models import User
from itertools import chain
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.template.loader import render_to_string, get_template

from django.utils.html import strip_tags

# Create your views here.
def welcome(request):
    context={}
    return HttpResponse("Welcome")

@login_required(login_url="/")
class ManagerView(ListView):
    model=investmoney
    template_name="kunai/proj-manager.html"
    context_object_name="queryset"
    paginate_by = 50

    def get_context_data(self, **kwargs):
        investments_available = investmoney.objects.all()
        context={
            "invest":investments_available,
        }
        return context


@login_required(login_url="/")
def show_all_projects(request):
    OtherActivities = others.objects.filter(is_active=True).order_by('name')
    PayFess = feesandbills.objects.filter(is_active=True).order_by('name')
    BuyLand = buyland.objects.filter(is_active=True).order_by('name')
    BuyHouse_list= buyhouse.objects.filter(is_active=True).order_by('name')
    BuyEquipment = buyitem.objects.filter(is_active=True).order_by('name')
    DonateMoney = donatemoney.objects.filter(is_active=True).order_by('name')
    InvestMoney= investmoney.objects.filter(is_active=True).order_by('name')
    Buildhouse= buildhouse.objects.filter(is_active=True).order_by('name')
    result_list = list(chain(InvestMoney, Buildhouse, DonateMoney, BuyEquipment, BuyHouse_list, BuyLand, PayFess, OtherActivities))
    context={"projects":result_list}
    return render(request, 'kunai/proj-manager.html', context)

@login_required(login_url="/")
def show_pending_projects(request):
    OtherActivities = others.objects.filter(is_active=False).order_by('name')[:12]
    PayFess = feesandbills.objects.filter(is_active=False).order_by('name')[:12]
    BuyLand = buyland.objects.filter(is_active=False).order_by('name')[:12]
    BuyHouse_list= buyhouse.objects.filter(is_active=False).order_by('name')[:12]
    BuyEquipment = buyitem.objects.filter(is_active=False).order_by('name')[:12]
    DonateMoney = donatemoney.objects.filter(is_active=False).order_by('name')[:12]
    InvestMoney= investmoney.objects.filter(is_active=False).order_by('name')[:12]
    Buildhouse= buildhouse.objects.filter(is_active=False).order_by('name')[:12]
    result_list = list(chain(InvestMoney, Buildhouse, DonateMoney, BuyEquipment, BuyHouse_list, BuyLand, PayFess, OtherActivities))
    if result_list:
        projects = True
    else:
        projects = False
    users = User.objects.filter(is_staff=True)
    context={"InvestMoney":InvestMoney, "Buildhouse":Buildhouse, "DonateMoney":DonateMoney, "BuyEquipment":BuyEquipment, "BuyHouse":BuyHouse_list, "BuyLand":BuyLand, "PayFees":PayFess, "OtherActivities":OtherActivities, "projects":projects, "users":users}
    return render(request, 'kunai/pending.html', context)

def assign_agent(request):
    if request.is_ajax():
        agent = request.GET.get('agent_name')
        id = request.GET.get('project_id')
        type = request.GET.get('type')
        if type == 'invest_money':
            project = get_object_or_404(investmoney, id=id)
        elif type== 'build_house':
            project = get_object_or_404(buildhouse, id=id)
        elif type == 'donate_money':
            project = get_object_or_404(donatemoney, id=id)
        elif type == 'buy_equipment':
            project = get_object_or_404(buyitem, id=id)
        elif type == 'buy_house':
            project = get_object_or_404(buyhouse, id=id)
        elif type == 'pay_fees':
            project = get_object_or_404(feesandbills, id=id)
        elif type == 'buy_land':
            project = get_object_or_404(buyland, id=id)
        elif type == 'other':
            project = get_object_or_404(others, id=id)
        else:
            data ={"alert":"Invalid Request"}
            return JsonResponse(data)
        agent_to = get_object_or_404(User, username=agent)
        project.agent = agent_to
        project.save()
        data ={"alert":"The project was successfully assigned: "+agent}
        return JsonResponse(data)
    else:
        data = {"alert":"404: Error"}
        return JsonResponse(data)

@login_required(login_url="/")
def show_detail_about_pending(request, id):
    project = get_object_or_404(investmoney, id=id)
    context ={"project":project}
    return render(request,"kunai/pending_detail.html", context)

@login_required(login_url="/")
def show_client_activities(request):
    OtherActivities = others.objects.filter(agent=request.user).order_by('name')[:12]
    PayFess = feesandbills.objects.filter(agent=request.user).order_by('name')[:12]
    BuyLand = buyland.objects.filter(agent=request.user).order_by('name')[:12]
    BuyHouse_list= buyhouse.objects.filter(agent=request.user).order_by('name')[:12]
    BuyEquipment = buyitem.objects.filter(agent=request.user).order_by('name')[:12]
    DonateMoney = donatemoney.objects.filter(agent=request.user).order_by('name')[:12]
    InvestMoney= investmoney.objects.filter(agent=request.user).order_by('name')[:12]
    Buildhouse= buildhouse.objects.filter(agent=request.user).order_by('name')[:12]
    result_list = list(chain(InvestMoney, Buildhouse, DonateMoney, BuyEquipment, BuyHouse_list, BuyLand, PayFess, OtherActivities))
    if result_list:
        projects = True
    else:
        projects = False
    users = User.objects.filter(is_staff=True)
    context={"InvestMoney":InvestMoney, "Buildhouse":Buildhouse, "DonateMoney":DonateMoney, "BuyEquipment":BuyEquipment, "BuyHouse":BuyHouse_list, "BuyLand":BuyLand, "PayFees":PayFess, "OtherActivities":OtherActivities, "projects":projects, "users":users}
    return render(request, "kunai/clientActivity.html", context)

def send_agent_note(request):
    agent = request.GET.get("agent_name")
    client = request.GET.get("client_name")
    title = request.GET.get("title")
    body = request.GET.get("body")
    agent_obj = get_object_or_404(User, username=agent)
    client_obj = get_object_or_404(User, username=client)
    to = "wilsonmutebi41@gmail.com"

    ###############################
    #ctx = {
    #    'user': "Ajay"
    #}
    #message = get_template('mail.html').render(ctx)
    #msg = EmailMessage(
    #    'Subject',
    #    message,
    #    'from@example.com',
    #    ['to@example.com'],
    #)
    #msg.content_subtype = "html"  # Main content is now text/html
    #msg.send()

    #Creating notification email
    mail_data={"title":"Note from Reconna Agent","subject":title,"content":body, "sender":agent, "receiver":client}
    message = get_template('kunai/note_mail.html').render(mail_data)
    html_content = render_to_string("kunai/note_mail.html", )
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        "Note From Reconna Agent:",
        html_content,
        settings.EMAIL_HOST_USER,
        [to]
    )
    email.attach_alternative(text_content, "text/html")

    #Saving to the database
    new_note= notes(
        agent=agent_obj,
        client=client_obj,
        title =title,
        body = body,
        agent_status = 1,
        client_status =0,
    )
    new_note.save()
    data={'alert':"The note was sent successfully"}
    return JsonResponse(data)

@login_required(login_url="/")
def show_notes(request):
    client_notes = notes.objects.filter(agent=request.user, agent_status=False).order_by("-timer")
    context={"client_notes":client_notes}
    return render(request,"kunai/notes.html", context)

def agent_seen(request):
    id = request.GET.get('note_id')
    note = get_object_or_404(notes,id=id)
    note.agent_status=True
    note.save()
    data ={"alert":"success"}
    return JsonResponse(data)



def send_agent_comment(request):
    note_id = request.GET.get('note_id')
    body = request.GET.get('body')
    username = request.GET.get('user')
    user = get_object_or_404(User, username=username)
    comment_to_save = comment(
        body=body,
        username=user
    )
    comment_to_save.save()
    note = get_object_or_404(notes, id=note_id)
    note.comments.add(comment_to_save)
    note.client_status=False
    note.save()
    data={"alert":'success'}
    return JsonResponse(data)


def unread_agent_notes(request):
    if request.user.is_authenticated:
        total_unread= notes.objects.filter(agent=request.user, agent_status=False).count()
        return {"unread_agent_notes":total_unread}
    else:
        return {"unread_agent_notes":"0"}