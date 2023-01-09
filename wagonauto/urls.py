from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('companies/',views.CompanyListView.as_view(),name='clist'),
    path('suzuki/',views.SuzukiListView.as_view(),name='suzukilist'),
    path('hyundai/',views.HyundaiListView.as_view(),name='hyundailist'),
    path('tata/',views.TataListView.as_view(),name='tatalist'),
    path('toyota/',views.ToyotaListView.as_view(),name='toyotalist'),
    path('mahindra/',views.MahindraListView.as_view(),name='mahindralist'),
    path('honda/',views.HondaListView.as_view(),name='hondalist'),
    path('kia/',views.KiaListView.as_view(),name='kialist'),
    path('suzuki/<int:pk>/',views.SuzukiDetailView.as_view(),name='suzukidetail'),
    path('hyundai/<int:pk>/',views.HyundaiDetailView.as_view(),name='hyundaidetail'),
    path('tata/<int:pk>/',views.TataDetailView.as_view(),name='tatadetail'),
    path('toyota/<int:pk>/',views.ToyotaDetailView.as_view(),name='toyotadetail'),
    path('mahindra/<int:pk>/',views.MahindraDetailView.as_view(),name='mahindradetail'),
    path('honda/<int:pk>/',views.HondaDetailView.as_view(),name='hondadetail'),
    path('kia/<int:pk>/',views.KiaDetailView.as_view(),name='kiadetail'),
    path('contacts/',views.ContactPage.as_view(),name='contlist'),
]
