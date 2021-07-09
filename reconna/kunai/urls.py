from django.urls import path
from .views import *

app_name="kunai"

urlpatterns = [
    #path("", welcome, name="welcome"),
    #path("",ManagerView.as_view(), name="welcome" ),
    path("", show_all_projects, name="welcome"),
    path("Pending/Projects", show_pending_projects, name="pending_projects"),
    path("pending_detail/<str:id>", show_detail_about_pending, name="pending_detail"),
    path("ajax/assignAgent", assign_agent, name="asssign_agent"),
    path("showNotes/", show_notes, name="show_notes"),
    path("showAgentClients/", show_client_activities, name="show_client_activities")
]