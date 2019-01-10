from django.contrib import admin
from endereco.models import Endereco
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Endereco, SimpleHistoryAdmin)
