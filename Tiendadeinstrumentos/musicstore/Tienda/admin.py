
from django.contrib import admin

from .models import Instrumento


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "categoria",
        "precio",
        "descuento",
    )

    list_filter = (
        "categoria",
        "descuento",
    )

    search_fields = (
        "nombre",
        "categoria",
    )


