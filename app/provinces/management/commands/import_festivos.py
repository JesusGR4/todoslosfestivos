from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests
from provinces.models import Comunidad, Provincia, Municipio, Festivo
import time
import traceback
meses = {
    'enero': '01',
    'febrero': '02',
    'marzo': '03',
    'abril': '04',
    'mayo': '05',
    'junio': '06',
    'julio': '07',
    'agosto': '08',
    'septiembre': '09',
    'octubre': '10',
    'noviembre': '11',
    'diciembre': '12',
}
class Command(BaseCommand):
    help = 'Importación de provincias'

    def handle(self, *args, **options):
        for municipio in Municipio.objects.all():
            print(municipio.name)
            url = "https://fiestas.net"+municipio.scrapped_url
            print(url)
            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            list_festivos = soup.find(id="fiestas")
            if list_festivos:
                lis = list_festivos.find_all("li")
                pagination = soup.find(id="pagination").find_all(class_="button")
                last_page = int(pagination[len(pagination)-1].text)
                for li in lis:
                    try:
                        nombre = li.find("span", {"class": "name"}).text
                        if Festivo.objects.filter(name=nombre).exists():
                            continue
                        distancia = li.p.find("span", {"class": "distance"}).text if li.p.find("span", {"class": "distance"}) else "" 
                        ciudad_cercana = li.p.find("a", {"class": "town"}).text if li.p.find("a", {"class": "town"}) else ""
                        fechas_span = li.p.find("span", {"class": "dates"})
                        fecha_inicio = None
                        fecha_fin = None
                        if fechas_span and " al " in fechas_span.text:
                            fechas = fechas_span.text
                            fechas = fechas.replace("del", "").strip()
                            fechas_spliteadas = fechas.split(" al ")
                            dia = fechas_spliteadas[0].split(" de ")[0]
                            mes = meses.get(fechas_spliteadas[0].split(" de ")[1].lower(), '01')
                            fecha_inicio = f"2021-{mes}-{dia}"
                            dia = fechas_spliteadas[1].split(" de ")[0]
                            mes = meses.get(fechas_spliteadas[1].split(" de ")[1].lower(), '01')
                            fecha_fin = f"2021-{mes}-{dia}"
                                
                        elif fechas_span:
                            fechas = fechas_span.text.replace("(Aprox.)", "").strip()
                            dia = fechas.split(" de ")[0]
                            mes = meses.get(fechas.split(" de ")[1].lower(), '01')
                            fecha_inicio = f"2021-{mes}-{dia}"
                        Festivo.objects.create(
                            municipio=municipio,
                            name=nombre,
                            fecha_inicio=fecha_inicio,
                            fecha_fin=fecha_fin,
                            ciudad_cercana=ciudad_cercana,
                            distancia=distancia
                        )
                    except Exception as e:
                        print(traceback.format_exc())
                        continue
                i=2
                while i <= last_page:
                    url_ = "https://fiestas.net"+municipio.scrapped_url+f"{i}/"
                    print(url_)
                    req_ = requests.get(url_)
                    soup_ = BeautifulSoup(req_.content, 'html.parser')
                    list_festivos_ = soup_.find(id="fiestas")
                    if list_festivos_:
                        lis_ = list_festivos_.find_all("li")
                        for li_ in lis_:
                            try:
                                nombre_ = li_.find("span", {"class": "name"}).text
                                if Festivo.objects.filter(name=nombre_).exists():
                                    continue
                                distancia_ = li_.p.find("span", {"class": "distance"}).text if li_.p.find("span", {"class": "distance"}) else ""
                                ciudad_cercana_ = li_.p.find("a", {"class": "town"}).text if li_.p.find("a", {"class": "town"}) else ""
                                fechas_span_ = li_.p.find("span", {"class": "dates"})
                                fecha_inicio_ = None
                                fecha_fin_ = None
                                if fechas_span_ and " al " in fechas_span_.text:
                                    fechas_ = fechas_span_.text
                                    fechas_ = fechas_.replace("del", "").strip()
                                    fechas_spliteadas_ = fechas_.split(" al ")
                                    dia_ = fechas_spliteadas_[0].split(" de ")[0]
                                    mes_ = meses.get(fechas_spliteadas_[0].split(" de ")[1].lower(), '01')
                                    fecha_inicio_ = f"2021-{mes_}-{dia_}"
                                    dia_ = fechas_spliteadas_[1].split(" de ")[0]
                                    mes_ = meses.get(fechas_spliteadas_[1].split(" de ")[1].lower(), '01')
                                    fecha_fin_ = f"2021-{mes_}-{dia_}"
                                elif fechas_span_:
                                    fechas_ = fechas_span_.text.replace("(Aprox.)", "").strip()
                                    dia_ = fechas_.split(" de ")[0]
                                    mes_ = meses.get(fechas_.split(" de ")[1].lower(), '01')
                                    fecha_inicio_ = f"2021-{mes_}-{dia_}"
                                Festivo.objects.create(
                                    municipio=municipio,
                                    name=nombre_,
                                    fecha_inicio=fecha_inicio_,
                                    fecha_fin=fecha_fin_,
                                    ciudad_cercana=ciudad_cercana_,
                                    distancia=distancia_
                                )
                            except Exception as e:
                                print(traceback.format_exc())
                                continue
                    i+=1
