from django.shortcuts import render
from django.views.generic import DetailView, ListView
from product.models import Product

class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    model = Product

class ProductListView(ListView):
    template_name = "product/product_list.html"
    model = Product
    context_object_name = 'products'