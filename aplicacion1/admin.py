from django.contrib import admin

# Register your models here.
from aplicacion1.models import Jvconsultacontroller


class JvconsultacontrollerAdmin (admin.ModelAdmin):
    pass
admin.site.register(Jvconsultacontroller,JvconsultacontrollerAdmin)
