from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """renders cart + contents"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Adds quantity of a product to cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """
    Edits the quantity of a product within a cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart')) 