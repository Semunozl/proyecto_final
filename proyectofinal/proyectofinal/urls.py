from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from proyectofinal.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name = "index"),
    path("users/", include("users.urls")),
    path("categorias/", include("categories.urls")),
    path("products/", include("products.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)