from django.urls import path
from . import views

app_name = "catalog"


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/review/', views.ReviewCreateView.as_view(), name='add_review'),
    path('basket/add/', views.BasketCreateView.as_view(), name='basket_create'),
    path('basket/', views.BasketListView.as_view(), name='basket_list'),
    path('basket/<int:pk>/edit/', views.BasketUpdateView.as_view(), name='edit_basket'),
    path('basket/<int:pk>/delete/', views.BasketDeleteView.as_view(), name='delete_basket'),
]