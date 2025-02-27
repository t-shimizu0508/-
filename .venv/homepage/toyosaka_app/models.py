from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="タイトル")
    description = models.TextField(verbose_name="説明文")
    image = models.ImageField(upload_to='service_images/', verbose_name="画像")

    def __str__(self):
        return self.title