from django.urls import path
from .views import (
    AnzeigenListenAnsicht, 
    AnzeigenDetailAnsicht,
    AnzeigenAnlegenAnsicht,
    AnzeigenAktualisierenAnsicht,
    AnzeigenLoeschenAnsicht,
    BenutzerAnzeigenListenAnsicht,
    KategorienListenAnsicht
)
from . import views


urlpatterns = [
    path('', AnzeigenListenAnsicht.as_view(), name='anzeigen-home'),
    path('benutzer/<str:username>/', BenutzerAnzeigenListenAnsicht.as_view(), name='benutzer-anzeigen'),
    path('anzeige/<int:pk>/', AnzeigenDetailAnsicht.as_view(), name='anzeige-detail'),
    path('anzeige/neu/', AnzeigenAnlegenAnsicht.as_view(), name='anzeige-create'),
    path('anzeige/<int:pk>/aktualisieren/', AnzeigenAktualisierenAnsicht.as_view(), name='anzeige-update'),
    path('anzeige/<int:pk>/loeschen/', AnzeigenLoeschenAnsicht.as_view(), name='anzeige-delete'),
    path('kategorie/<int:pk>/', KategorienListenAnsicht.as_view(), name='anzeigen-kategorie'),
    path('about/', views.about, name='about'),
]

# path('kategorie/<int:pk>', KategorienListenAnsicht.as_view(), name='anzeigen-kategorie'),
#path('anzeige/kategorie/<str:kategorie_slug>/', KategorienListenAnsicht.as_view(), name='anzeigen-kategorie'),