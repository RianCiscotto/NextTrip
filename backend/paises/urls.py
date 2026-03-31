from django.urls import path
from .views import listar_paises
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('paises/', listar_paises),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


