from django.db import models
from django.urls import reverse, NoReverseMatch


class MenuItem(models.Model):
    menu_name = models.CharField(max_length=255, verbose_name="Название меню")
    title = models.CharField(max_length=255, verbose_name="Пункт меню")
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
        verbose_name="Родительский пункт"
    )
    url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Явный URL"
    )
    named_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Именованный URL"
    )

    class Meta:
        verbose_name = "Элемент меню"
        verbose_name_plural = "Элементы меню"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return '#'
        if self.url:
            return self.url
        return '#'
