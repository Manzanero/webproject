from django.db import models

class EntityTexture(models.Model):
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return f'{self.category}/{self.sub_category}/{self.code}'

    @property
    def path(self):
        return f'{self.category}/{self.sub_category}/{self.code}.png'
