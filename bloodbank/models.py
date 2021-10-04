from django.db.models.fields import NullBooleanField
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Person(models.Model):
    BLOOD_GROUPS_CHOICES = (
        ('a_positive', 'A+'),
        ('a_negative', 'A-'),
        ('b_positive', 'B+'),
        ('b_negative', 'B-'),
        ('o_positive', 'O+'),
        ('o_negative', 'O-'),
        ('ab_positive', 'AB+'),
        ('ab_negative', 'AB-'),
    )

    GENDER_CHOICES = (
        ('m', _('Male')),
        ('f', _('Female'))
    )

    name        =   models.CharField(_('Name'), max_length=128)
    dob         =   models.DateField(_('Date of birth'))
    gender      =   models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES)

    blood_group =   models.CharField(_('Blood Group'), max_length=16, choices=BLOOD_GROUPS_CHOICES)

    phone       =   models.CharField(_('Phone Number'), max_length=12)
    alt_phone   =   models.CharField(_('Alternative Phone Number'), max_length=12, null=True, blank=True)
    address     =   models.CharField(_('Address'), max_length=256)
    facebook    =   models.URLField(_('Facebook'), null=True, blank=True)

    photo       =   models.ImageField(upload_to='photos/', null=True, blank=True)

    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True, blank=True, null=True)