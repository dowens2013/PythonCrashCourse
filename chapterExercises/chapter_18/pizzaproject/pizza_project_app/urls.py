"""Define URLs for pizza project"""

from django.urls import path

from . import views

app_name = "pizza_project_app"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    # Pizza toppings
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]