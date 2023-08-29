from django.shortcuts import render, redirect

from django.views.generic import ListView

from app.models import Product, Contact


class IndexView(ListView):
    template_name = 'index.html'
    model = Product


def detail(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    context = {
        'product': product
    }
    return render(request, 'secend web site/adomla/product_detail.html', context)


def odamla(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'secend web site/adomla/index.html', context)


def about(request):
    return render(request, 'secend web site/for navbar/about.html')


def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        contact = Contact(first_name=first_name, last_name=last_name,
                          email=email, phone_number=phone_number, message=message)
        contact.save()
        return redirect('index')
    return render(request, 'secend web site/for navbar/contact.html')


def index(request):
    return render(request, 'secend web site/for navbar/index.html')
