from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.User_login,name='index'),
    path('create_user',views.User_create,name="create_user"),
    path('product_list', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart_view'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
     path('bill/<int:order_id>/', views.generate_bill_pdf, name='download_bill'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)