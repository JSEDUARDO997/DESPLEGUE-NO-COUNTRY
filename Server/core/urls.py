from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path('auth/', include('djoser.urls')),  # Rutas de autenticación básicas
    path('auth', include('djoser.urls.jwt')),  # Rutas de JWT 
    
    path('api/product/', include('apps.product.urls')),
    path('api/cart/', include('apps.cart.urls')),
    path('api/message/', include('apps.message.urls')),
    
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
