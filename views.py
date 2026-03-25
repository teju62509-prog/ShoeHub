from django.shortcuts import render, get_object_or_404, redirect
from .models import Shoe

# Home page
def home(request):
    category = request.GET.get('category')  # filter by ?category=Men etc.
    if category:
        shoes = Shoe.objects.filter(category=category)
    else:
        shoes = Shoe.objects.all()
    return render(request, 'home.html', {'shoes': shoes})

# Shoe detail page
def shoe_detail(request, id):
    shoe = get_object_or_404(Shoe, id=id)
    return render(request, 'shoe_detail.html', {'shoe': shoe})

# Add to cart (session-based)
def add_to_cart(request, id):
    shoe = get_object_or_404(Shoe, id=id)
    cart = request.session.get('cart', {})
    if str(shoe.id) in cart:
        cart[str(shoe.id)]['quantity'] += 1
    else:
        cart[str(shoe.id)] = {
            'name': shoe.name,
            'price': float(shoe.price),
            'quantity': 1
        }
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('view_cart')

# Increase quantity
def increase_quantity(request, id):
    cart = request.session.get('cart', {})
    shoe_id = str(id)
    if shoe_id in cart:
        cart[shoe_id]['quantity'] += 1
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('view_cart')

# Decrease quantity
def decrease_quantity(request, id):
    cart = request.session.get('cart', {})
    shoe_id = str(id)
    if shoe_id in cart:
        cart[shoe_id]['quantity'] -= 1
        if cart[shoe_id]['quantity'] <= 0:
            del cart[shoe_id]  # remove item if quantity 0
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('view_cart')

# View cart page
def view_cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total': total})

# views.py
def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']  # remove cart completely
        request.session.modified = True
    return redirect('view_cart')  # go back to cart page

# Contact page
def contact(request):
    return render(request, 'contact.html')

# About page
def about(request):
    return render(request, 'about.html')

# Help Desk page
def helpdesk(request):
    return render(request, 'help.html')

def landing(request):
    return render(request, 'index.html')