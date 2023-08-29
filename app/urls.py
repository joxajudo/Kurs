from django.urls import path

from app.views import IndexView, detail, contact, about, odamla

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('product_detail/<int:product_id>', detail, name='product_detail'),

    path('kurs', odamla, name='odam')

]
