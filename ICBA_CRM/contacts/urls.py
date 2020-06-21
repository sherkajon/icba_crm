from django.urls import  path
from . import views

urlpatterns = [
    path('contact/', views.contact),
    path('organization/', views.organization),
    path('organization/new_org/', views.add_New_Organization)
]