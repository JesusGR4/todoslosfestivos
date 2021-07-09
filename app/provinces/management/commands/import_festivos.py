from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests
from provinces.models import Comunidad, Provincia, Municipio
import time


class Command(BaseCommand):
    help = 'Importación de provincias'

    def handle(self, *args, **options):
        for municipio in Municipio.objects.all():
            url = "https://fiestas.net"+municipio.scrapped_url
            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            list_festivos = soup.find(id="fiestas")
            lis = list_festivos.find_all("li")
            for li in lis:
                print(li.p.text)