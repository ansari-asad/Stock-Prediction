from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('stock', views.stock, name='stock')
]

from pred import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)