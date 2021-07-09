from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests
from provinces.models import Comunidad, Provincia, Municipio
import time


class Command(BaseCommand):
    help = 'Importación de provincias'

    def handle(self, *args, **options):
        
        for provincia in Provincia.objects.all():
            url = "https://fiestas.net"+provincia.scrapped_url+"municipios"
            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            list_municipios = soup.find(id="places").find_all("li")
            for municipio in list_municipios:
                try:
                    nombre = municipio.a.text
                    if Municipio.objects.filter(name=nombre).exists():
                        continue
                    href = municipio.a['href']
                    url = "https://fiestas.net"+href
                    req = requests.get(url)
                    soup_ = BeautifulSoup(req.content, 'html.parser')
                    div_map = soup_.find(id="map")
                    latitude = div_map["data-latitude"]
                    longitude = div_map["data-longitude"]
                    place_info_div = soup_.find(id="placeInfo").find_all("li")
                    population_div = soup_.find(id="population")
                    pagina_oficial=place_info_div[4].a['href']
                    Municipio.objects.create(
                        name=nombre,
                        num_habitantes=population_div.text,
                        provincia=provincia,
                        pagina_oficial=pagina_oficial,
                        latitude=latitude,
                        longitude=longitude,
                        scrapped_url=href
                    )
                    print(nombre + " introducida")
                    time.sleep(2)
                except Exception as e:
                    print("error")
                    continue
            
            
        print("Todas las provincias guardadas")