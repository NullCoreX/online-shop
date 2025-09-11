from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='all'),
    path('<int:pk>', views.ProductDetailView.as_view(), name="product_detail"),
    path('navbar', views.NavbarPartialView.as_view(), name="navbar"),

    path('category', views.CategoryView.as_view(), name="category"),
    path('category/<slug:slug>', views.CategoryItemsView.as_view(), name="category_items"),
]
