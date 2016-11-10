from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.CartDetail.as_view(), name="cart_detail"),
	url(r'^add/(?P<product_id>\d+)/$', views.AddProduct.as_view(), name="cart_add"),
	url(r'^remove/(?P<product_id>\d+)/$', views.Remove.as_view(), name="cart_remove"),
	#url(r'^prueba/(?P<product_id>\d+)/$', views.Prueba.as_view(), name="prueba")
]