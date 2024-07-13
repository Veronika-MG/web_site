from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path("admin", admin.site.urls),
    path("auth/", include("auth.urls")),
    path("", include("homepage.urls")),
    path("services/", include("services.urls")),
    path("reviews/", include("reviews.urls")),
    path("user/", include("user.urls")),
    path("about/", include("about.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
