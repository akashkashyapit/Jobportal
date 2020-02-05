from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import  static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("shop/", include('shop.urls')),
    # path("blog/", include('blog.urls')),

    # rest_framework api
    path('api/', include('api.urls'), name='api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
