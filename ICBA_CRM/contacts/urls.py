from django.urls import  path
from . import views

urlpatterns = [
    path('contact/', views.contact),
    path('organization/', views.organization),
    path('organization/new_org/', views.add_New_Organization),
    path('contact/new_contact/', views.add_New_Contact),
    path('contact/update_contact/<str:pk>/', views.updateContact, name="update_contact"),
    path('contact/<int:pk>/delete/', views.deleteContact, name="delete_contact"),
    path('organization/update_organization/<str:pk>/', views.updateOrganization, name="update_organization"),
    path('organization/<int:pk>/delete/', views.deleteOrganization, name='delete_organization')

]