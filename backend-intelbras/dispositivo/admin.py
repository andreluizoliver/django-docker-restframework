from django.contrib import admin
from dispositivo.models import Dispositivo
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Dispositivo, SimpleHistoryAdmin)
