from django.db import models

# Create your models here.

class hotel(models.Model):
    Hotel_name = models.CharField(max_length=200)
    stars = models.BigIntegerField()
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    pic = models.FileField(null=True, blank=True)
    facilities = models.CharField(max_length=200)
    lattitude = models.CharField(max_length=200)
    contact = models.BigIntegerField()
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=250)




    def __str__(self):
        return self.Hotel_name


class department(models.Model):
    department = models.CharField(max_length=200)
    hotels_id = models.ForeignKey(hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.department



class employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    pic = models.FileField(null=True, blank=True)
    job = models.CharField(max_length=200)
    work_email = models.CharField(max_length=200)
    work_mobile = models.BigIntegerField()
    work_iemi = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    martial_status = models.CharField(max_length=200)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    mail_id = models.CharField(max_length=200)
    mobile = models.BigIntegerField()
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    depart = models.ForeignKey(department, on_delete=models.CASCADE)
    hotels = models.ForeignKey(hotel, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name