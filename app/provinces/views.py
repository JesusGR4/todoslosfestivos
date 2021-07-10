from django.shortcuts import render, redirect
from provinces.models import Comunidad, Provincia, Municipio, Festivo
from django.core.paginator import Paginator


def home_view(request):
    comunidades = Comunidad.objects.all()
    festivos_mas_cercanos = Festivo.objects.order_by('fecha_inicio')[:10]
    provincias = Provincia.objects.all()[:5]
    return render(request, 'home.html', {'comunidades': comunidades,
                                         'festivos': festivos_mas_cercanos,
                                         'provincias': provincias})


def comunidad_view(request, pk):
    comunidades = Comunidad.objects.all()
    comunidad_seleccionada = Comunidad.objects.get(pk=pk)
    festivos = Festivo.objects.filter(municipio__provincia__comunidad=comunidad_seleccionada).order_by('fecha_inicio')
    paginator = Paginator(festivos, 10)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    provincias = Provincia.objects.filter(comunidad=comunidad_seleccionada)[:4]
    return render(request, 'comunidad.html', {'comunidades': comunidades,
                                              'festivos': festivos,
                                              'comunidad_seleccionada': comunidad_seleccionada,
                                              'provincias': provincias,
                                              'page_obj': page_obj})


def provincia_view(request, pk):
    comunidades = Comunidad.objects.all()
    provincia = Provincia.objects.get(pk=pk)
    comunidad_seleccionada = provincia.comunidad
    festivos = Festivo.objects.filter(municipio__provincia=provincia).order_by('fecha_inicio')
    paginator = Paginator(festivos, 10)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    provincias = Provincia.objects.filter(comunidad=comunidad_seleccionada).exclude(pk=provincia.pk)[:4]
    return render(request, 'provincia.html', {'comunidades': comunidades,
                                              'festivos': festivos,
                                              'comunidad_seleccionada': comunidad_seleccionada,
                                              'provincias': provincias,
                                              'provincia_seleccionada': provincia,
                                              'page_obj': page_obj})


def provincia_municipios_view(request, pk):
    comunidades = Comunidad.objects.all()
    provincia = Provincia.objects.get(pk=pk)
    comunidad_seleccionada = provincia.comunidad
    provincias = Provincia.objects.filter(comunidad=comunidad_seleccionada).exclude(pk=provincia.pk)[:4]
    municipios = Municipio.objects.filter(provincia=provincia)
    return render(request, 'provincia_municipios.html', {'comunidades': comunidades,
                                                         'comunidad_seleccionada': comunidad_seleccionada,
                                                         'provincias': provincias,
                                                         'provincia_seleccionada': provincia,
                                                         'municipios': municipios}
                  )


def municipio_view(request, pk):
    comunidades = Comunidad.objects.all()
    municipio = Municipio.objects.get(pk=pk)
    comunidad_seleccionada = municipio.provincia.comunidad
    festivos = Festivo.objects.filter(municipio=municipio).order_by('fecha_inicio')
    paginator = Paginator(festivos, 10)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    provincias = Provincia.objects.filter(comunidad=comunidad_seleccionada).exclude(pk=municipio.provincia.pk)[:4]
    return render(request, 'municipio.html', {'comunidades': comunidades,
                                              'festivos': festivos,
                                              'municipio_seleccionado': municipio,
                                              'comunidad_seleccionada': comunidad_seleccionada,
                                              'provincias': provincias,
                                              'page_obj': page_obj})
