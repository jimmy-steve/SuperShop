from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from store.models import Product, Cart, Order

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        # email = request.POST.get("email")
        # name = request.POST.get("name")
        # message = request.POST.get("message")
        # contact_method = request.POST.get("contact_method")
        # priority = request.POST.get("priority")

        # Ajout de la logique d'envoi d'email
        # send_mail(
        #     subject=f"Nouveau message de {name} (priorité {priority})",
        #     message=f"Message: {message}\nContact via: {contact_method}",
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[settings.DEFAULT_FROM_EMAIL],
        # )
        messages.success(request, "Votre message a été envoyé avec succès.")
        return redirect('contact')
    return render(request, 'contact.html')


def index(request):
    products = Product.objects.all()

    return render(request, 'store/index.html', context={"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product": product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)

    return render(request, "store/cart.html", context={"orders": cart.orders.all()})


def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()

    return redirect('index')

