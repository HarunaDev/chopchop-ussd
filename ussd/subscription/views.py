from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

# disable CSRF protection for this view to allow USSD requests without CSRF token verification
@csrf_exempt
def index(request):
    # check if the request method is POST
    if request.method == 'POST':
        # get the neccesary parameters from the POST request
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text', '')