from django.contrib import admin
from usuario.models import Usuario
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Usuario, SimpleHistoryAdmin)
