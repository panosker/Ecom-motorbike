from django.urls import path

from . import views

urlpatterns = [
	
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('store_item/<int:pk>',views.store_item , name = 'store_item' ),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]