from django.contrib import admin
from .models import Desktop
from import_export.admin import ImportExportModelAdmin


@admin.register(Desktop)
class ViewAdmin(ImportExportModelAdmin):
    pass
