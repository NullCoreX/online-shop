from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='all'),
    path('<int:pk>', views.ProductDetailView.as_view(), name="product_detail"),
]
