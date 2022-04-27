from django.db import models

# Create your models here.

#image upload test
class plantUpload(models.Model):
    plant_main_img=models.ImageField(upload_to='images/')

class plant(models.Model):
    Common_Name=models.CharField(max_length=100)
    Scientific_Name=models.CharField(max_length=100, primary_key=True)
    Family=models.CharField(max_length=50)
    SubFamily=models.CharField(max_length=60)

    def __str__(self):
        return self.Common_Name

class Area(models.Model):
    area_id=models.AutoField(primary_key=True)
    Scientific_Name=models.ForeignKey('plant',on_delete=models.CASCADE)
    Abundant_Area=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.area_id

class Treatment(models.Model):
    treatment_id=models.AutoField(primary_key=True)
    treatment_method=models.CharField(max_length=1000)

    def __str__(self):
        return self.treatment_id




