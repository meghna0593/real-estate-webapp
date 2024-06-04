from apps.common.models import TimeStampedUUIDModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Enquiry(TimeStampedUUIDModel):
    name = models.CharField(_("Your Name"), max_length=100)
    phone_number = PhoneNumberField(_("Phone Number"), max_length=15)
    email = models.EmailField(_("Email"))
    subject = models.CharField(_("Subjecy"), max_length=100)
    message = models.TextField(_("Message"))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = _("Enquiries")
