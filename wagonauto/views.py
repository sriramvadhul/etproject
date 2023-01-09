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

class SuzukiDetailView(DetailView):
    context_object_name = 'suzukidet'
    model = models.Suzuki
    template_name = 'wagonauto/suzuki_detail.html'

class HyundaiDetailView(DetailView):
    context_object_name = 'hyundaidet'
    model = models.Hyundai
    template_name = 'wagonauto/hyundai_detail.html'

class TataDetailView(DetailView):
    context_object_name = 'tatadet'
    model = models.Tata
    template_name = 'wagonauto/tata_detail.html'

class ToyotaDetailView(DetailView):
    context_object_name = 'toyotadet'
    model = models.Toyota
    template_name = 'wagonauto/toyota_detail.html'

class MahindraDetailView(DetailView):
    context_object_name = 'mahindradet'
    model = models.Mahindra
    template_name = 'wagonauto/mahindra_detail.html'

class HondaDetailView(DetailView):
    context_object_name = 'hondadet'
    model = models.Honda
    template_name = 'wagonauto/honda_detail.html'

class KiaDetailView(DetailView):
    context_object_name = 'kiadet'
    model = models.Kia
    template_name = 'wagonauto/kia_detail.html'

class ContactPage(TemplateView):
    template_name = 'wagonauto/contacts.html'
