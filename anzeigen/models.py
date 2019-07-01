from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Anzeigen Model

class Anzeige(models.Model):
    titel = models.CharField(max_length=100)
    inhalt = models.TextField()
    erstellungsdatum = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    kategorie = models.ForeignKey(
        'Kategorie', 
        on_delete=models.SET_NULL,
        null=True)
    

    class Meta:
        verbose_name_plural = 'Anzeigen'

    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse('anzeige-detail', kwargs={'pk': self.pk})




class Kategorie(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorien'

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('anzeige-kategorie', kwargs={'pk': self.pk, 'slug': self.slug})
