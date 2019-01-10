from django.contrib import admin
from visitante.models import Visitante
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Visitante, SimpleHistoryAdmin)
