from django.shortcuts import render
from .models import Pizza


def index(request):
    """Home page"""
    return render(request, 'pizza_project_app/index.html')


def pizzas(request):
    """Pizza page"""
    pizza = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizza}
    return render(request, 'pizza_project_app/pizzas.html', context)


def pizza(request, pizza_id):
    """Toppings page"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizza_project_app/pizza.html', context)
