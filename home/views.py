from django.shortcuts import render
from django.views.generic import TemplateView
from product.models import Product

class Home(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all products (or limit if you want)
        context['products'] = Product.objects.all()[:8]  # Or Product.objects.all()[:8] for latest 8
        return context
