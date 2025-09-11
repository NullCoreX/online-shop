from gc import get_objects

from django.shortcuts import render , redirect , get_object_or_404
from django.views import View

from product.models import Product
from .cart_module import Cart


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request,'cart/cart_detail.html',{'cart':cart})
# Create your views here.


class CartAddView(View):
    def post(self, request, pk):
        # print('product added')
        product = get_object_or_404(Product , id=pk)
        size,color,quantity = request.POST.get('size'),request.POST.get('color'),request.POST.get('quantity')
        # print(size,color,quantity)
        cart = Cart(request)
        cart.add(product,quantity,color,size)
        return redirect('cart:cart_detail')

