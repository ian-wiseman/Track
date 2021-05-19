from django.shortcuts import render
from .models import Recruiter, Placement
from .forms import RecruiterCreateForm, PlacementCreateForm
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, "home.html")

class RecruiterList(ListView):
    model = Recruiter
    template_name = "track_app/recruiter_list.html"

class PlacementList(ListView):
    model = Placement
    template_name = "track_app/placement_list.html"

class RecruiterCreate(CreateView):
  model = Recruiter
  form_class = RecruiterCreateForm
  template_name = "track_app/recruiter_create_form.html"
  success_url ="/"

class PlacementCreate(CreateView):
  model = Placement
  form_class = PlacementCreateForm
  template_name = "track_app/placement_create_form.html"
  success_url ="/"

class RecruiterUpdate(UpdateView):
  model = Recruiter
  form_class = RecruiterCreateForm
  template_name = "track_app/recruiter_update_form.html"
  success_url ="/"
  
class PlacementUpdate(UpdateView):
  model = Placement
  form_class = PlacementCreateForm
  template_name = "track_app/placement_update_form.html"
  success_url ="/"

class PlacementDelete(DeleteView):
  model = Placement
  template_name = "track_app/placement_delete_form.html"
  success_url ="/"
  
