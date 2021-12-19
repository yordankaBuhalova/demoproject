from django.db import models
from django.contrib.auth.models import User
from enum import Enum
import uuid
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Language(models.Model):
    """
    Model representing one language.
    Attributes:
        language, lang_abbreviation, created_date, modified_date
    """
    language = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        verbose_name=_("Language name")
    )
    lang_abbreviation = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        verbose_name=_("Language abbreviation")
    )
    created_date = models.DateField(auto_now_add=True, verbose_name=_("Created date"))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_("Last modified date"))

    def __str__(self):
        return self.language

    class Meta:

        verbose_name = _("Language")
        verbose_name_plural = _("Languages")


class ClientFirm(models.Model):
    """
    Model representing the client/firm which orders a project
    Attributes:
        name, country, city, address, created_date, modified_date
    """
    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        verbose_name=_("Client name")
    )
    email = models.EmailField(verbose_name=_("Email"))
    country = models.CharField(max_length=255, verbose_name=_("Country"))
    city = models.CharField(max_length=45, verbose_name=_("City"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    created_date = models.DateField(auto_now_add=True, verbose_name=_("Created date"))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_("Last modified date"))

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = _("Client")
        verbose_name_plural = _("Clients")


class Project(models.Model):
    """
    Model which represents a project conducted with the Generator
    Attributes:
        name, client, user, language,
        text, created_date, modified_date
    """
    name = models.CharField(
        max_length=30, verbose_name=_("Project name"), unique=True
    )
    client = models.ForeignKey(
        ClientFirm,
        on_delete=models.CASCADE,
        related_name='cprojekts',
        verbose_name=_("Client")
    )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Autor")
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        verbose_name=_("Language")
    )
    text = models.TextField(max_length=300, verbose_name=_("Description"))
    created_date = models.DateField(auto_now_add=True, verbose_name=_("Created date"))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_("Last modified date"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")




