from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models

# Create your views here.
def index(request):
    return render(request,'wagonauto/index.html')

class CompanyListView(ListView):
    context_object_name = 'company'
    model = models.Companies

class SuzukiListView(ListView):
    context_object_name = 'suzuki'
    model = models.Suzuki

class HyundaiListView(ListView):
    context_object_name = 'hyundai'
    model = models.Hyundai

class TataListView(ListView):
    context_object_name = 'tata'
    model = models.Tata

class ToyotaListView(ListView):
    context_object_name = 'toyota'
    model = models.Toyota

class MahindraListView(ListView):
    context_object_name = 'mahindra'
    model = models.Mahindra

class HondaListView(ListView):
    context_object_name = 'honda'
    model = models.Honda

class KiaListView(ListView):
    context_object_name = 'kia'
    model = models.Kia
