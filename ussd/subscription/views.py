from django.shortcuts import render # type: ignore
from django.views.decorators.csrf import csrf_exempt # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.

# disable CSRF protection for this view to allow USSD requests without CSRF token verification
@csrf_exempt
def index(request):
    # check if the request method is POST
    if request.method == 'POST':
        # get the neccesary parameters from the POST request
        session_id = request.POST.get('sessionId', None)
        serviceCode = request.POST.get('serviceCode', None)
        phone_number = request.POST.get('phoneNumber', None)
        text = request.POST.get('text', '') # provide a default value of empty string if 'text' is not provided

        #process the ussd request and generate a response based on the text input, we will do this inside of a function called handle_ussd_request
        response = handle_ussd_request(text)

        # return the generated response as an HTTP response
        return HttpResponse(response)
    else:
        return HttpResponse("Invalid request method", status=405)
# initialize a cart to keep track of selected orders 
cart = []

# define a dictionary to store items with their prices
menu = {
    "1*1": {"name": "Rice & 1pc Chicken", "price": 2700, "quantity": 0},
    "1*2": {"name": "Spaghetti & 1pc Chicken", "price": 2400, "quantity": 0},
    "1*3": {"name": "Burger Suya", "price": 2000, "quantity": 0},
    "1*4": {"name": "Chicken & Chips", "price": 2500, "quantity": 0},
    "2*1": {"name": "Fruit Smoothie", "price": 1500, "quantity": 0},
    "2*2": {"name": "Yoghurt", "price": 1000, "quantity": 0},
    "2*3": {"name": "Water", "price": 300, "quantity": 0},
    "3*1": {"name": "Burger Suya & Fruit Smoothie", "price": 3500, "quantity": 0},
    "3*2": {"name": "Rice & 3pcs Chicken", "price": 5300, "quantity": 0},
    "3*3": {"name": "Small Chops & 3pcs Chicken", "price": 4900, "quantity": 0},
}


# function to handle the logic of the ussd request based on the user's input 
def handle_ussd_request(text):
    #if no text input(initial request), display the main menu
    if text == "":
        return f'''
CON Welcome to Choji Food Shop, Select an option to get your meal
1. Order Food
2. Order Drinks
3. Special Combo Menu
4. Contact Us
{"5. Checkout" if cart else ''}
'''     
        
    # if the user selects '1', show Order Food options
    elif text == "1":
        return f'''
CON Select from the option to order food
1. Rice & 1pc Chicken @2700
2. Spagetti & 1pc Chicken @2400
3. Burger Suya @2000
4. Chicken & Chips @2500
5. Order Drinks
6. Main Menu
{"7. Checkout" if cart else ''}
'''
    # if the user selects '1*1', show option to continue shopping or checkout
#   elif text == "1*1":
#       return f'''
# CON choose an option
# 1. Order more
# 2. Checkout
# '''

    # if the user selects '2', show option to order drinks
    elif text == "2":
        return f'''
CON Select from the drinks options
1. Fruit Smoothie @1500
2. Yoghurt @1000
3. Water @300
4. Main menu
{"5. Checkout" if cart else ''}
'''
    
    # if the user selects '3', show option to special combo
    elif text == "3":
        return f'''
CON Select from the special combo options 
1. Burger Suya & Fruit Smoothie @3500
2. Rice & 3pcs Chicken @5300
3. Small Chops & 3pcs Chicken @4900
4. Main Menu
{"5. Checkout" if cart else ""}
'''
    
    # if the user selects '4', show option to contact us
    elif text == "4":
        return f'''
CON Contact Us @
- Call our lines 080800300 090300800
- Send us a mail chojischops@food.com
1. Main Menu
{"2. Checkout" if cart else ""}
'''