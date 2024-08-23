from django.urls import path
from .views import test_ussd

urlpatterns = [
    path('test_ussd/', test_ussd, name='test_ussd'),
]
