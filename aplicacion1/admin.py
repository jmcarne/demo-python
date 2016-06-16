from django.contrib import admin

# Register your models here.
from aplicacion1.models import Jvconsultacontroller, Sensor


class JvconsultacontrollerAdmin (admin.ModelAdmin):
    pass
admin.site.register(Jvconsultacontroller,JvconsultacontrollerAdmin)


class SensorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sensor, SensorAdmin)
