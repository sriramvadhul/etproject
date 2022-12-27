from django.db import models

# Create your models here.
class Companies(models.Model):
    company_name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='company_logos')

    def __str__(self):
        return self.company_name

class Suzuki(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='suzuki_cars')
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.car_name

class Hyundai(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='hyundai_cars')
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.car_name

class Tata(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='tata_cars')
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.car_name

class Toyota(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='toyota_cars')
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.car_name

class Mahindra(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='mahindra_cars')
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.car_name

class Honda(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='honda_cars')
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.car_name

class Kia(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='kia_cars')
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.car_name
