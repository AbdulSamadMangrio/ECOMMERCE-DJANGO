from tkinter.font import names
from . import views
from django.urls import path
from .views import OrderListCreateView, PaymentListCreateView, ProductListCreateView, OrderRetrieveUpdateDestroyView, \
    PaymentRetrieveUpdateDestroyView, ProductRetrieveUpdateDestroyView, LogoutView, LoginView, home_view, register_user
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
    path('api/orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-retrieve-update-destroy'),
    path('api/payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('api/payments/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-retrieve-update-destroy'),
    path('api/register/', register_user, name='register_user'),
    path('api/token/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout_view'),
    path('checkout/', views.checkout, name='payment_form'),
    path('success/', views.success, name='success'),
]
