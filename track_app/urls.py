"""track_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recruiter/list", views.RecruiterList.as_view(), name="recruiterlist"),
    path("placement/list", views.PlacementList.as_view(), name="placementlist"),
    path("recruiter/create", views.RecruiterCreate.as_view(), name="recruitercreate"),
    path("placement/create", views.PlacementCreate.as_view(), name="placementcreate"),
    path("recruiter/create", views.RecruiterCreate.as_view(), name="recruitercreate"),
    path("placement/update/<pk>", views.PlacementUpdate.as_view(), name="placementupdate"),
    path("recruiter/update/<pk>", views.RecruiterUpdate.as_view(), name="recruiterupdate"),
    path("placement/delete/<pk>", views.PlacementDelete.as_view(), name="placementdelete")
]

