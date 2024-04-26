from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Item

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request, 'ecommerce/index.html', {'items' : items})

def add_to_cart(request, item_id):
    pass
