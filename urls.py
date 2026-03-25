from django.urls import path
from . import views  

urlpatterns = [
    path('', views.landing, name='landing'),  # Landing page at /
    path('home/', views.home, name='home'),   # Actual home page
    path('shoes/<int:id>/', views.shoe_detail, name='shoe_detail'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('cart/increase/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('help/', views.helpdesk, name='helpdesk'),
]