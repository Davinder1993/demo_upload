from django.shortcuts import render
from shop.models import *
# Create your views here.

def index(request):
    product=Product.objects.all()
    context={'product': product}
    print(product)
    return render(request, 'shop/index.html',context)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def search(request):
    return render(request, 'shop/search.html')

def product_view(request):
    
    return render(request, 'shop/product_view.html')


def check_out(request):
    return render(request, 'shop/check_out.html')

def tracker(request):
    return render(request, 'shop/tracker.html')





