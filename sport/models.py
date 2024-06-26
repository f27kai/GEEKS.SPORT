from django.db import models

class Slogan(models.Model):
    text = models.CharField(max_length=200, verbose_name="Слоган")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Слоган"
        verbose_name_plural = "Слоган"

class YouTube(models.Model):
    url_youtube = models.URLField(verbose_name="Ссылка на ютуб")
    slogan = models.ForeignKey(Slogan, on_delete=models.CASCADE, verbose_name="Слоган")

    def __str__(self):
        return self.url_youtube

    class Meta:
        verbose_name = "Ютуб"
        verbose_name_plural = "Ютуб"