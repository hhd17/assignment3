from django.urls import path
from .views import create_contact, contact_list, contact_detail, update_contact, delete_contact, home, success, dateerror

app_name = 'myapp1'

urlpatterns = [
    path('success/', success, name='success'),
    path('dateerror/', dateerror, name='dateerror'),
    path('contact/', contact_list, name='contact_list'),
    path('contact/<int:pk>/', contact_detail, name='contact_detail'),
    path('contact/<int:pk>/update/', update_contact, name='update_contact'),
    path('contact/<int:pk>/delete/', delete_contact, name='delete_contact'), 
    path('create/', create_contact, name='create_contact'),
    path('', home, name='home')
]