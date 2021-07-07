from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('provinces.urls')),
    path('admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    # only for development!
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)