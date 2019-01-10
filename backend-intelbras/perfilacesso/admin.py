from django.contrib import admin
from perfilacesso.models import PerfilAcesso
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(PerfilAcesso, SimpleHistoryAdmin)
