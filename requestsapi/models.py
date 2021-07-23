from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Customers(models.Model):
    # Пользователи

    name = models.TextField()
    email = models.TextField(null=True, unique=True)
    telegram = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

class Staff(models.Model):
    # Сотрудники

    name = models.TextField()
    email = models.TextField(null=True, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'

class RequestStatusChoices(models.TextChoices):
    """Статусы заявки"""

    OPEN = "OPEN", "Открыта"
    CLOSED = "CLOSED", "Закрыта"
    INWORK = "IN WORK", "В работе"


class Request(models.Model):
    """Заявка"""

    title = models.TextField()
    description = models.TextField(default='', blank=True)
    status = models.TextField(
        choices=RequestStatusChoices.choices,
        default=RequestStatusChoices.OPEN
    )
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='request')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='request', null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    objects = models.Manager()

    def __str__(self):
        return f"{self.title} - {self.customer}"

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'
