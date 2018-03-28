from django.conf.urls import url
from products.views import ProductListView, ProductDetailView

urlpatterns = [
	url(r'^$', ProductListView.as_view(),name='products'),
	url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(),name='detail'),
]

