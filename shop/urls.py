from django.urls import path
from shop.views import *
urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('search/',search,name='search'),
    path('checkout/',check_out,name='checkout'),
    path('product-view/',product_view,name='product'),
    path('tracker/',tracker,name='tracker'),
]
