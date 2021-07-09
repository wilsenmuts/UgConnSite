from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from flashcards.models import *
from django.contrib.auth.models import User
from itertools import chain
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

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

@login_required(login_url="/")
def show_notes(request):
    context={}
    return render(request,"kunai/notes.html", context)