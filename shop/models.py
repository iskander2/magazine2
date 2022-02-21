from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name="Название")

    class Meta:
        verbose_name ="Категория"
        verbose_name_plural = "категорий"
    def __str__(self):
        return self.name

class Category2(models.Model):
    name =models.CharField(max_length=50,verbose_name="название")
    price = models.DecimalField(max_digits=500, decimal_places=2,verbose_name="Цена")
    description =models.CharField(max_length=200,verbose_name="описание")
    image=models.ImageField(upload_to="images",verbose_name="Картинка")

    class Meta:
        verbose_name="Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
         return self.name                  