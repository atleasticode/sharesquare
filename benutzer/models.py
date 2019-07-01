from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profil(models.Model):
    benutzer = models.OneToOneField(User, on_delete=models.CASCADE)
    profil_bild = models.ImageField(default='default.jpg', upload_to='profilbilder')

    def __str__(self):
        return f'{self.benutzer.username} Profil'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profil_bild.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profil_bild.path)
