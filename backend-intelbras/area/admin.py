from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from area.models import Area


admin.site.register(Area, SimpleHistoryAdmin)