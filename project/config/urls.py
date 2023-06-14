from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("home.urls", "home"))),
    path('crear-anuncio/', include(("post.urls", 'crear-anuncio')))

]
