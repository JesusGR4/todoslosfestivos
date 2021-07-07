from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests
from provinces.models import Comunidad, Provincia
import time


class Command(BaseCommand):
    help = 'Importación de provincias'

    def handle(self, *args, **options):
        
        for comunidad in Comunidad.objects.all():
            url = "https://fiestas.net"+comunidad.scrapped_url
            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            list_provincias = soup.find_all(class_="level2")
            for provincia in list_provincias:
                nombre = provincia.a.text
                href = provincia.a['href']
                url = "https://fiestas.net"+href
                req = requests.get(url)
                soup_ = BeautifulSoup(req.content, 'html.parser')
                div_map = soup_.find(id="map")
                latitude = div_map["data-latitude"]
                longitude = div_map["data-longitude"]
                place_info_div = soup_.find(id="placeInfo").find_all("li")
                pagina_oficial=place_info_div[4].a['href']
                Provincia.objects.create(
                    name=nombre,
                    comunidad=comunidad,
                    pagina_oficial=pagina_oficial,
                    latitude=latitude,
                    longitude=longitude,
                    scrapped_url=href
                )
                print(nombre + " introducida")
                time.sleep(2)
            
            
        print("Todas las provincias guardadas")