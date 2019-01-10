from django.contrib import admin
from zonatempo.models import ZonaTempo, Tempo
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(ZonaTempo, SimpleHistoryAdmin)
admin.site.register(Tempo, SimpleHistoryAdmin)
