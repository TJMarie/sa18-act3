from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
"""
def home(request):
    return render(request, 'pages/home.html')

def show(request):
    return render(request, 'pages/show.html')
"""
def product_list(request):
    products = Product.objects.all()
    return render(request, 'pages/home.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'pages/show.html', {'product': product})