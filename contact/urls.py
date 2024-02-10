from django.urls import path
from .views import create_contact ,list_contacts

urlpatterns = [
    path('create/', create_contact, name='create-contact'),
      path('list/', list_contacts, name='list-contacts'),
]
