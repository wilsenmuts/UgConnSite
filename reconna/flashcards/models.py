from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="clientprofiles/")
    contact = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    facebook = models.URLField(max_length=200)


class Deck(models.Model):
    title=models.CharField(max_length=64, null= False, blank=False)
    decsription = models.CharField(max_length=225, null=False, blank=False)

    def __str__(self):
        return self.title

class Card(models.Model):
    parentDeck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    front = models.TextField()
    back = models.TextField()

    def __str__(self):
        return self.front
'''
class users(models.Model):
    firstname = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    username = models.CharField(max_length=35)
    email = models.CharField(max_length=35 )
    password = models.CharField(max_length = 35)

    def __str__(self):
        return self.username

    def get_total(self):
        total = self.buildhouse_set.count()
        return str(total)
    get_total.short_description='buildcount'
    '''

class buildhouse(models.Model):
    name = models.CharField(max_length=50, default="Buildhouse")
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    reside= models.CharField(max_length=35)
    structure = models.CharField(max_length=35)
    serviceprovider = models.CharField(max_length=35 )
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    #assign_agent = models.CharField(max_length=50, blank=True)
    agent = models.ForeignKey(User, related_name="builh_agent", on_delete=models.SET_NULL, null=True, limit_choices_to={"is_staff":True})

    def __str__(self):
        return self.reside

class buyhouse(models.Model):
    name = models.CharField(max_length=50, default="BuyHouse")
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    reside= models.CharField(max_length=35)
    structure = models.CharField(max_length=35)
    serviceprovider = models.CharField(max_length=35 )
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    #assign_agent = models.CharField(max_length=50, blank=True)
    agent = models.ForeignKey(User, related_name="buyh_agent", on_delete=models.SET_NULL, null=True, limit_choices_to={"is_staff":True})

    def __str__(self):
        return self.name

class investmoney(models.Model):
    name = models.CharField(max_length=50, default="investmoney")
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    title= models.CharField(max_length=35)
    activity = models.CharField(max_length=35)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    #assign_agent = models.CharField(max_length=50, blank=True)
    #assign_agent_link = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    agent = models.ForeignKey(User, related_name="invest_agent", on_delete=models.SET_NULL, null=True, limit_choices_to={"is_staff":True})

    def __str__(self):
        return self.title

class buyland(models.Model):
    name = models.CharField(max_length=50, default="BuyLand")
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    reside= models.CharField(max_length=35)
    structure = models.CharField(max_length=35)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    #assign_agent = models.CharField(max_length=50, blank=True)
    agent = models.ForeignKey(User, related_name="bul_agent", on_delete=models.SET_NULL, null=True, limit_choices_to={"is_staff":True})

    def __str__(self):
        return self.reside

class donatemoney(models.Model):
    name = models.CharField(max_length=50, default="DonateMoney")
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    orgname= models.CharField(max_length=35)
    activity = models.CharField(max_length=35)
    reside = models.CharField(max_length=35 )
    contact = models.CharField(max_length=35 )
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    #assign_agent = models.CharField(max_length=50, blank=True)
    agent = models.ForeignKey(User, related_name="donate_agent", on_delete=models.SET_NULL, null=True, limit_choices_to={"is_staff":True})

    def __str__(self):
        return self.orgname

class feesandbills(models.Model):
    name = models.CharField(max_length=50, default="FeesAndBills")
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    activity = models.CharField(max_length=35)
    amount = models.CharField(max_length=35 )
    payplan = models.FileField(upload_to='plans')
    receiver = models.CharField(max_length=35 )
    receiver_contact = models.CharField(max_length=20, default="")
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    #assign_agent = models.CharField(max_length=50, blank=True)
    agent = models.ForeignKey(User, related_name="pay_agent", on_delete=models.SET_NULL, null=True, limit_choices_to={"is_staff":True})

    def __str__(self):
        return self.name

class buyitem(models.Model):
    name = models.CharField(max_length=50, default="BuyItems")
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    item = models.CharField(max_length=35)
    quantity = models.CharField(max_length=35)
    quality = models.CharField(max_length=35 )
    receiver = models.CharField(max_length=35 )
    contact = models.CharField(max_length=35)
    reside = models.CharField(max_length=35)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    #assign_agent = models.CharField(max_length=50, blank=True)
    agent = models.ForeignKey(User, related_name="equip_agent", on_delete=models.SET_NULL, null=True, limit_choices_to={"is_staff":True})

    def __str__(self):
        return self.item

class others(models.Model):
    name = models.CharField(max_length=50, default="OtherActivities")
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    activity= models.CharField(max_length=35)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    #assign_agent = models.CharField(max_length=50, blank=True)
    agent = models.ForeignKey(User, related_name="other_agent", on_delete=models.SET_NULL, null=True, limit_choices_to={"is_staff":True})

    def __str__(self):
        return self.activity

class grieve(models.Model):
    title= models.CharField(max_length=35)
    about = models.CharField(max_length = 700)
    notes = models.TextField()

    def __str__(self):
        return self.grieve


class article(models.Model):
    author = models.CharField(max_length=35, default='Ugconn')
    title= models.CharField(max_length=35)
    about = models.CharField(max_length=35)
    date_as_is = models.DateField()
    site = models.URLField( max_length=300)
    notes = models.TextField()

    def __str__(self):
        return self.title

class about(models.Model):
    title = models.CharField(max_length=50)
    describe = models.TextField(blank=True)
    reside = models.CharField(max_length=250, blank=True)
    contact = models.CharField(max_length=250, blank=True)
    watsapp  = models.CharField(max_length=250, blank=True)
    email  = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title

class service(models.Model):
    title = models.CharField(max_length=50)
    describe = models.TextField(blank=True)
    status = models.BooleanField()
    link = models.URLField()

    def __str__(self):
        return self.title
    