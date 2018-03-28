from django.conf.urls import url , include
from django.contrib import admin
from .views import home_page,contact_page,login_page,register_page,SearchProduct,logout_view
from cart.views import cart_home,cart_update

urlpatterns = [
	url(r'^$', home_page,name='home'),
	#url(r'^about/$', about_page,name="about"),
	url(r'^products/', include("products.urls")),
	url(r'^search/', SearchProduct.as_view(),name='search'),
	#url(r'^search/?q=(?P<query_search>/w+)$', SearchProduct.as_view(),name='search'),
	url(r'^login/$', login_page,name="login"),
	url(r'^logout/$', logout_view,name="logout"),
	url(r'^register/$', register_page,name="register"),
	url(r'^contact/', contact_page,name='contact'),
    url(r'^admin/', admin.site.urls),
    url(r'^cart/$', cart_home,name="cart"),
    url(r'^cart/update/$', cart_update,name="cartupdate"),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
