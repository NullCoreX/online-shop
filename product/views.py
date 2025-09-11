
from django.views.generic import DetailView, ListView, TemplateView
from product.models import Product, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q

class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    model = Product

class ProductListView(ListView):
    template_name = "product/product_list.html"
    model = Product
    context_object_name = 'products'

class NavbarPartialView(TemplateView):
    template_name = "includes/nav_bar.html"
    def get_context_data(self, **kwargs):
        context = super(NavbarPartialView,self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
class CategoryView(TemplateView):
    template_name = "category/category_list.html"
    def get_context_data(self, **kwargs):
        context = super(CategoryView,self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

class CategoryItemsView(ListView):
    template_name = "category/category_items.html"
    context_object_name = 'products'
    model = Product

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(categories=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context





class ProductSearchView(ListView):
    template_name = "product/product_list.html"  # reuse the product list template
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Product.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return Product.objects.all()  # show all if no search term
