from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("home.urls", "index"))),
    path('post/', include(("post.urls", 'index')))

]
