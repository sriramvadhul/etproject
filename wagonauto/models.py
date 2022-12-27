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
    price = models.CharField(max_length=30)
    about = models.TextField(default = "About")
    engine_type = models.CharField(max_length=64,default="Type 0")
    max_power = models.CharField(max_length=64,default="0 @ 0rpm")
    max_torque = models.CharField(max_length=64,default="0 @ 0rpm")
    no_cylinders = models.PositiveIntegerField(default = 0)
    valves_per_cylinder = models.PositiveIntegerField(default = 0)
    transmission_type = models.CharField(max_length=64,default="Automatic")
    gear_box = models.CharField(max_length=64,default="5 gears")
    fuel_type = models.CharField(max_length=64,default="P/D/C")
    mileage = models.FloatField(default = 0)
    tank_capacity = models.FloatField(default = 0)
    emission_norm = models.CharField(max_length=64,default="BS IV")
    length = models.PositiveIntegerField(default = 0)
    width = models.PositiveIntegerField(default = 0)
    weight = models.PositiveIntegerField(default = 0)
    height = models.PositiveIntegerField(default = 0)
    boot_space = models.PositiveIntegerField(default = 0)
    seating = models.PositiveIntegerField(default = 0)
    others = models.TextField(default = "Others")

    def __str__(self):
        return self.car_name

class Hyundai(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='hyundai_cars')
    price = models.CharField(max_length=20)
    about = models.TextField(default = "About")
    engine_type = models.CharField(max_length=64,default="Type 0")
    max_power = models.CharField(max_length=64,default="0 @ 0rpm")
    max_torque = models.CharField(max_length=64,default="0 @ 0rpm")
    no_cylinders = models.PositiveIntegerField(default = 0)
    valves_per_cylinder = models.PositiveIntegerField(default = 0)
    transmission_type = models.CharField(max_length=64,default="Automatic")
    gear_box = models.CharField(max_length=64,default="5 gears")
    fuel_type = models.CharField(max_length=64,default="P/D/C")
    mileage = models.FloatField(default = 0)
    tank_capacity = models.FloatField(default = 0)
    emission_norm = models.CharField(max_length=64,default="BS IV")
    length = models.PositiveIntegerField(default = 0)
    width = models.PositiveIntegerField(default = 0)
    weight = models.PositiveIntegerField(default = 0)
    height = models.PositiveIntegerField(default = 0)
    boot_space = models.PositiveIntegerField(default = 0)
    seating = models.PositiveIntegerField(default = 0)
    others = models.TextField(default = "Others")

    def __str__(self):
        return self.car_name

class Tata(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='tata_cars')
    price = models.CharField(max_length=20)
    about = models.TextField(default = "About")
    engine_type = models.CharField(max_length=64,default="Type 0")
    max_power = models.CharField(max_length=64,default="0 @ 0rpm")
    max_torque = models.CharField(max_length=64,default="0 @ 0rpm")
    no_cylinders = models.PositiveIntegerField(default = 0)
    valves_per_cylinder = models.PositiveIntegerField(default = 0)
    transmission_type = models.CharField(max_length=64,default="Automatic")
    gear_box = models.CharField(max_length=64,default="5 gears")
    fuel_type = models.CharField(max_length=64,default="P/D/C")
    mileage = models.FloatField(default = 0)
    tank_capacity = models.FloatField(default = 0)
    emission_norm = models.CharField(max_length=64,default="BS IV")
    length = models.PositiveIntegerField(default = 0)
    width = models.PositiveIntegerField(default = 0)
    weight = models.PositiveIntegerField(default = 0)
    height = models.PositiveIntegerField(default = 0)
    boot_space = models.PositiveIntegerField(default = 0)
    seating = models.PositiveIntegerField(default = 0)
    others = models.TextField(default = "Others")

    def __str__(self):
        return self.car_name

class Toyota(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='toyota_cars')
    price = models.CharField(max_length=20)
    about = models.TextField(default = "About")
    engine_type = models.CharField(max_length=64,default="Type 0")
    max_power = models.CharField(max_length=64,default="0 @ 0rpm")
    max_torque = models.CharField(max_length=64,default="0 @ 0rpm")
    no_cylinders = models.PositiveIntegerField(default = 0)
    valves_per_cylinder = models.PositiveIntegerField(default = 0)
    transmission_type = models.CharField(max_length=64,default="Automatic")
    gear_box = models.CharField(max_length=64,default="5 gears")
    fuel_type = models.CharField(max_length=64,default="P/D/C")
    mileage = models.FloatField(default = 0)
    tank_capacity = models.FloatField(default = 0)
    emission_norm = models.CharField(max_length=64,default="BS IV")
    length = models.PositiveIntegerField(default = 0)
    width = models.PositiveIntegerField(default = 0)
    weight = models.PositiveIntegerField(default = 0)
    height = models.PositiveIntegerField(default = 0)
    boot_space = models.PositiveIntegerField(default = 0)
    seating = models.PositiveIntegerField(default = 0)
    others = models.TextField(default = "Others")

    def __str__(self):
        return self.car_name

class Mahindra(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='mahindra_cars')
    price = models.CharField(max_length=20)
    about = models.TextField(default = "About")
    engine_type = models.CharField(max_length=64,default="Type 0")
    max_power = models.CharField(max_length=64,default="0 @ 0rpm")
    max_torque = models.CharField(max_length=64,default="0 @ 0rpm")
    no_cylinders = models.PositiveIntegerField(default = 0)
    valves_per_cylinder = models.PositiveIntegerField(default = 0)
    transmission_type = models.CharField(max_length=64,default="Automatic")
    gear_box = models.CharField(max_length=64,default="5 gears")
    fuel_type = models.CharField(max_length=64,default="P/D/C")
    mileage = models.FloatField(default = 0)
    tank_capacity = models.FloatField(default = 0)
    emission_norm = models.CharField(max_length=64,default="BS IV")
    length = models.PositiveIntegerField(default = 0)
    width = models.PositiveIntegerField(default = 0)
    weight = models.PositiveIntegerField(default = 0)
    height = models.PositiveIntegerField(default = 0)
    boot_space = models.PositiveIntegerField(default = 0)
    seating = models.PositiveIntegerField(default = 0)
    others = models.TextField(default = "Others")

    def __str__(self):
        return self.car_name

class Honda(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='honda_cars')
    price = models.CharField(max_length=20)
    about = models.TextField(default = "About")
    engine_type = models.CharField(max_length=64,default="Type 0")
    max_power = models.CharField(max_length=64,default="0 @ 0rpm")
    max_torque = models.CharField(max_length=64,default="0 @ 0rpm")
    no_cylinders = models.PositiveIntegerField(default = 0)
    valves_per_cylinder = models.PositiveIntegerField(default = 0)
    transmission_type = models.CharField(max_length=64,default="Automatic")
    gear_box = models.CharField(max_length=64,default="5 gears")
    fuel_type = models.CharField(max_length=64,default="P/D/C")
    mileage = models.FloatField(default = 0)
    tank_capacity = models.FloatField(default = 0)
    emission_norm = models.CharField(max_length=64,default="BS IV")
    length = models.PositiveIntegerField(default = 0)
    width = models.PositiveIntegerField(default = 0)
    weight = models.PositiveIntegerField(default = 0)
    height = models.PositiveIntegerField(default = 0)
    boot_space = models.PositiveIntegerField(default = 0)
    seating = models.PositiveIntegerField(default = 0)
    others = models.TextField(default = "Others")

    def __str__(self):
        return self.car_name

class Kia(models.Model):
    car_name = models.CharField(max_length=20)
    car_pic = models.ImageField(upload_to='kia_cars')
    price = models.CharField(max_length=20)
    about = models.TextField(default = "About")
    engine_type = models.CharField(max_length=64,default="Type 0")
    max_power = models.CharField(max_length=64,default="0 @ 0rpm")
    max_torque = models.CharField(max_length=64,default="0 @ 0rpm")
    no_cylinders = models.PositiveIntegerField(default = 0)
    valves_per_cylinder = models.PositiveIntegerField(default = 0)
    transmission_type = models.CharField(max_length=64,default="Automatic")
    gear_box = models.CharField(max_length=64,default="5 gears")
    fuel_type = models.CharField(max_length=64,default="P/D/C")
    mileage = models.FloatField(default = 0)
    tank_capacity = models.FloatField(default = 0)
    emission_norm = models.CharField(max_length=64,default="BS IV")
    length = models.PositiveIntegerField(default = 0)
    width = models.PositiveIntegerField(default = 0)
    weight = models.PositiveIntegerField(default = 0)
    height = models.PositiveIntegerField(default = 0)
    boot_space = models.PositiveIntegerField(default = 0)
    seating = models.PositiveIntegerField(default = 0)
    others = models.TextField(default = "Others")

    def __str__(self):
        return self.car_name
