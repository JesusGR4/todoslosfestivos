from django.urls import path, reverse_lazy
from provinces.views import home_view, comunidad_view, provincia_view, provincia_municipios_view, municipio_view

urlpatterns = [
    path('', home_view),
    path('comunidad/<int:pk>/', comunidad_view),
    path('provincia/<int:pk>/', provincia_view),
    path('municipio/<int:pk>/', municipio_view),
    path('provincia/<int:pk>/municipios/', provincia_municipios_view),
]
