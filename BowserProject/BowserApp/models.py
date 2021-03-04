from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Manager(AbstractUser):
    address1 = models.CharField(verbose_name=_('Address line 1'),max_length=1024,blank=True,null=True)
    address2 = models.CharField(verbose_name=_('Address line 2'),max_length=1024,blank=True,null=True)
    zip_code = models.CharField(verbose_name=_('Postal code'),max_length=12,blank=True,null=True)
    date_of_birth = models.DateField(verbose_name=_('Date of birth'),blank=True,null=True)
    company = models.CharField(verbose_name=_('Company'),max_length=1024,blank=True,null=True)
