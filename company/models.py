from django.db import models

class Company(models.Model):
    TYPE_CHOICES = [
        ('LLC', 'Limited Liability Company'),
        ('CORP', 'Corporation'),
        ('SOLE', 'Sole Proprietorship'),
        ('PART', 'Partnership'),
    ]

    REGION_CHOICES = [
        ('NCR', 'National Capital Region'),
        ('CAR', 'Cordillera Administrative Region'),
        ('Region I', 'Ilocos Region'),
        ('Region II', 'Cagayan Valley'),
        ('Region III', 'Central Luzon'),
        ('Region IV-A', 'CALABARZON'),
        ('Region IV-B', 'MIMAROPA Region'),
        ('Region V', 'Bicol Region'),
        ('Region VI', 'Western Visayas'),
        ('Region VII', 'Central Visayas'),
        ('Region VIII', 'Eastern Visayas'),
        ('Region IX', 'Zamboanga Peninsula'),
        ('Region X', 'Northern Mindanao'),
        ('Region XI', 'Davao Region'),
        ('Region XII', 'SOCCSKSARGEN'),
        ('Region XIII', 'Caraga'),
        ('BARMM', 'Bangsamoro Autonomous Region in Muslim Mindanao'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    address = models.TextField()
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=20, choices=REGION_CHOICES)
