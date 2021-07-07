from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests
from provinces.models import Comunidad
import time


class Command(BaseCommand):
    help = 'Importación de comunidades'

    def handle(self, *args, **options):
        url = "https://fiestas.net"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        list_comunidades = soup.find_all(class_="level1")
        
        for comunidad in list_comunidades:
            nombre = comunidad.a.text
            href = comunidad.a['href']
            req = requests.get(url + href)
            soup_ = BeautifulSoup(req.content, 'html.parser')
            div_map = soup_.find(id="map")
            latitude = div_map["data-latitude"]
            longitude = div_map["data-longitude"]
            place_info_div = soup_.find(id="placeInfo").find_all("li")
            Comunidad.objects.create(
                name=nombre,
                latitude=latitude,
                longitude=longitude,
                pagina_oficial=place_info_div[4].a['href'],
                scrapped_url=href
            )
            print(nombre + " introducida")
            time.sleep(2)
        print("Todas las comunidades impresas")