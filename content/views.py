from django.shortcuts import render

def home(reqest):
    return render(reqest, 'content/main_p.html')

def delivery(reqest):
    return render(reqest, 'content/delivery.html')

def payment(reqest):
    return render(reqest, 'content/payment.html')

def guarantee(reqest):
    return render(reqest, 'content/guarantee.html')

def public_offer(reqest):
    return render(reqest, 'content/public_offer.html')

def repairs(reqest):
    return render(reqest, 'content/repairs.html')

def exchange(reqest):
    return render(reqest, 'content/exchange.html')


def cart_used(reqest):
    return render(reqest, 'content/cart_used.html')
