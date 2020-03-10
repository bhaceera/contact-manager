from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    PARTNER = 'Partner'
    STAFF = 'Staff'
    ADMINISTRATION = 'Administration'
    AVITECH = 'Avitech'
    DEVOPS = 'Devops'
    EDUTECH = 'Edutech'
    ENGINEERING = 'Engineering Operations'
    FINANCE = 'Finance'
    FINATECH = 'Finatech'
    GARDEN = 'Garden Data'
    SHARED = 'Shared Resource'
    SOCIAL = 'Garden Social Ventures'
    HNI = 'HNI'
    LEGAL = 'Legal'
    POWERTECH = 'Powertech'
    PEOPLE = 'People Operations'
    SECURITY = 'Security'
    VENTURE = 'Venture Garden Group'
    VIGIPAY = 'Vigipay'
    SEX = ( (MALE, 'Male'), (FEMALE, 'Female'), )
    STATUS = ( (PARTNER, 'Partner'), (STAFF, 'Staff'), )
    SBU = ( (ADMINISTRATION, 'Administration'), (AVITECH, 'Avitech'), (DEVOPS, 'Devops'),
            (EDUTECH, 'Edutech'), (ENGINEERING, 'Engineering Operations'), (FINANCE, 'Finance'),
            (FINATECH, 'Finatech'), (GARDEN, 'Garden Data'), (SOCIAL, 'Garden Social Ventures'),
            (HNI, 'HNI'), (LEGAL, 'Legal'), (POWERTECH, 'Powertech'), (PEOPLE, 'People Operations'),
            (SECURITY,'Security'), (SHARED, 'Shared Resource'), (VENTURE, 'Venture Garden Group'), (VIGIPAY,'Vigipay'),
          )

    name = models.CharField(max_length= 30)
    email = models.EmailField()
    phone = models.CharField(max_length= 12)
    address = models.CharField(max_length= 200)
    sex = models.CharField(max_length= 10, choices=SEX, )
    sbu = models.CharField(max_length = 30, choices=SBU, )
    position = models.CharField(max_length = 30)
    status = models.CharField(max_length = 10, choices=STATUS,)
    # image = models.ImageField(default='key.jpg')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})


class Customer(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    ADMINISTRATION = 'Administration'
    AVITECH = 'Avitech'
    DEVOPS = 'Devops'
    EDUTECH = 'Edutech'
    ENGINEERING = 'Engineering Operations'
    FINANCE = 'Finance'
    FINATECH = 'Finatech'
    GARDEN = 'Garden Data'
    SHARED = 'Shared Resource'
    SOCIAL = 'Garden Social Ventures'
    HNI = 'HNI'
    LEGAL = 'Legal'
    POWERTECH = 'Powertech'
    PEOPLE = 'People Operations'
    SECURITY = 'Security'
    VENTURE = 'Venture Garden Group'
    VIGIPAY = 'Vigipay'
    SEX = ( (MALE, 'Male'), (FEMALE, 'Female'), )
    SBU = ( (ADMINISTRATION, 'Administration'), (AVITECH, 'Avitech'), (DEVOPS, 'Devops'),
            (EDUTECH, 'Edutech'), (ENGINEERING, 'Engineering Operations'), (FINANCE, 'Finance'),
            (FINATECH, 'Finatech'), (GARDEN, 'Garden Data'), (SOCIAL, 'Garden Social Ventures'),
            (HNI, 'HNI'), (LEGAL, 'Legal'), (POWERTECH, 'Powertech'), (PEOPLE, 'People Operations'),
            (SECURITY,'Security'), (SHARED, 'Shared Resource'), (VENTURE, 'Venture Garden Group'), (VIGIPAY,'Vigipay'),
          )

    name = models.CharField(max_length= 30)
    email = models.EmailField()
    phone = models.CharField(max_length= 12)
    address = models.CharField(max_length= 200)
    sex = models.CharField(max_length= 10, choices=SEX, )
    sbu = models.CharField(max_length = 30, choices=SBU, )
    position = models.CharField(max_length = 30)
    company = models.CharField(max_length = 200, null=True)
    # image = models.ImageField(default='key.jpg')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={'pk': self.pk})
