from django.contrib import admin
from departamento.models import Departamento
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Departamento, SimpleHistoryAdmin)
