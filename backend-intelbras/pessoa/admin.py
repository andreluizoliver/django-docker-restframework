from django.contrib import admin
from pessoa.models import Pessoa
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Pessoa, SimpleHistoryAdmin)
