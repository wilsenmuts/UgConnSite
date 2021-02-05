from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    reside= models.CharField(max_length=35)
    structure = models.CharField(max_length=35)
    serviceprovider = models.CharField(max_length=35 )
    brief = models.CharField(max_length = 700)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.reside

class buyhouse(models.Model):
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    reside= models.CharField(max_length=35)
    structure = models.CharField(max_length=35)
    serviceprovider = models.CharField(max_length=35 )
    description = models.CharField(max_length = 700)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.reside

class investmoney(models.Model):
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    title= models.CharField(max_length=35)
    activity = models.CharField(max_length=35)
    notes = models.CharField(max_length = 700)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class buyland(models.Model):
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    reside= models.CharField(max_length=35)
    structure = models.CharField(max_length=35)
    notes = models.CharField(max_length = 700)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.reside

class donatemoney(models.Model):
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    orgname= models.CharField(max_length=35)
    activity = models.CharField(max_length=35)
    reside = models.CharField(max_length=35 )
    contact = models.CharField(max_length=35 )
    notes = models.CharField(max_length = 700)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.orgname

class feesandbills(models.Model):
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    activity = models.CharField(max_length=35)
    amount = models.CharField(max_length=35 )
    payplan = models.FileField(upload_to='plans')
    receiver = models.CharField(max_length=35 )
    notes = models.CharField(max_length = 700)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.activity

class buyitem(models.Model):
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    item = models.CharField(max_length=35)
    quantity = models.CharField(max_length=35)
    quality = models.CharField(max_length=35 )
    receiver = models.CharField(max_length=35 )
    contact = models.CharField(max_length=35)
    reside = models.CharField(max_length=35)
    notes = models.CharField(max_length = 700)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.item

class others(models.Model):
    username =models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    activity= models.CharField(max_length=35)
    notes = models.CharField(max_length = 700)
    is_active = models.BooleanField(default=False)

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
    