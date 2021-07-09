from django.db import models
from django.contrib.auth.models import User
from django.db.models import aggregates
from flashcards.models import *

# Create your models here.

class comment(models.Model):
    username = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    body = models.TextField()
    agent_status = models.BooleanField(default=False) #Has agent read the note
    client_status = models.BooleanField(default=False) #Has client read the note
    timer = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.timer


class notes(models.Model):
    agent = models.CharField(max_length=45)
    client = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    title = models.CharField(max_length=45)
    body = models.TextField()
    agent_status = models.BooleanField(default=False) #Has agent read the note
    client_status = models.BooleanField(default=False) #Has client read the note
    comments = models.ManyToManyField(comment)
    timer = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title


class history(models.Model):
    start = models.DateField(auto_now_add=False)
    end = models.DateTimeField(auto_now=False, blank=True)
    activity = models.CharField(max_length=45)
    notes = models.TextField()

class bank(models.Model):
    activity = models.CharField(max_length=20)
    notes = models.TextField(blank=True)
    amount = models.IntegerField(default=0)
    remain = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=False)
    issuer = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    timezone = models.CharField(max_length=36)


class youtube(models.Model):
    name = models.CharField(max_length=50, default="")
    describe = models.TextField(blank=True)
    url_channel = models.URLField()
    timer = models.DateTimeField(auto_now_add=False)

class meeting(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    notes = models.TextField()
    type = models.CharField(max_length=20)


class project(models.Model):
    code = models.CharField(max_length=45, unique=True)
    client = models.CharField(max_length=45)
    agent = models.CharField(max_length=45)
    agent_notes = models.TextField() #the agent's notes after initialization meeting with client
    estimated_time = models.CharField(max_length=10)
    timeline = models.ManyToManyField(history)#stages of the project
    meeting_type = models.CharField(max_length=20) #chating or conferencing (other options will be welcome)
    previous_meeting = models.ManyToManyField(meeting)
    next_meeting = models.DateTimeField(auto_now=False)
    meeting_const = models.BooleanField(default=False) #False for meeting time being constant, no is for differences in meeting time
    budget_timeline = models.ManyToManyField(bank)
    notes = models.ManyToManyField(notes)
    activity_docs = models.FileField(upload_to="projectDocs/", blank=True)
    google_doc = models.URLField(blank=True)
    media = models.ManyToManyField(youtube)







