from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.

class Manager(AbstractUser):
    address1 = models.CharField(verbose_name=_("Addess line 1"),max_length=1024, blank=True,null=True)
    address2 = models.CharField(verbose_name=_("Addess line 2"),max_length=1024, blank=True,null=True)
    zip_code = models.CharField(verbose_name=_('Postal code'),max_length=12,blank=True,null=True)
    date_of_birth = models.DateField(verbose_name=_('Date of birth'),blank=True,null=True)
    company = models.CharField(verbose_name=_('Company Name'),max_length=1024,blank=True,null=True)

class Employee(models.Model):
    emp_manager = models.ForeignKey(Manager,models.SET_NULL,blank=True,null=True, related_name="manager", )
    emp_id = models.CharField(verbose_name=_("ID"),max_length=10,blank=False,null=False,unique=True)
    emp_email = models.EmailField(verbose_name=_("Email"))
    emp_first_name = models.CharField(verbose_name=_('First name'),max_length=132)
    emp_last_name = models.CharField(verbose_name=_('Last name'),max_length=132)
    emp_password = models.CharField(verbose_name=_('Password'),max_length=132)
    emp_address1 = models.CharField(verbose_name=_("Addess line 1"),max_length=1024, blank=True,null=True)
    emp_address2 = models.CharField(verbose_name=_("Addess line 2"),max_length=1024, blank=True,null=True)
    emp_zip_code = models.CharField(verbose_name=_('Postal code'),max_length=12,blank=True,null=True)
    emp_city = models.CharField(verbose_name=_('City'),max_length=132,blank=True,null=True)
    emp_date_of_birth = models.DateField(verbose_name=_('Date of birth'),blank=True,null=True)
    emp_company = models.CharField(verbose_name=_('Company Name'),max_length=1024,blank=True,null=True)
    emp_mobile_no = models.CharField(verbose_name=_('Mobile Number'),max_length=12)

    class Meta:
        ordering = ('-emp_id',)

    def get_absolute_url(self):
        return reverse('emp_detail',kwargs={'pk':self.pk})
