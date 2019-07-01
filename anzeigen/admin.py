from django.contrib import admin
from .models import Anzeige, Kategorie

# Anzeigen
admin.site.register(Anzeige)
admin.site.register(Kategorie)

