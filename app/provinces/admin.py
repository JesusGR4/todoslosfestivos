from django.contrib import admin
from . import models


admin.site.register(models.XperifunUser)
admin.site.register(models.Comunidad)
admin.site.register(models.Provincia)
admin.site.register(models.Municipio)
admin.site.register(models.Festivo)


