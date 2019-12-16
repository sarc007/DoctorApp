from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from multiselectfield import MultiSelectField
from Pathology.choices import *


class Patient_Details(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Age = models.PositiveIntegerField()
    Gender = models.CharField(max_length=120, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=10, unique=True)
    time = models.DateTimeField(default=datetime.now(), blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Name)


class Image_Input(models.Model):
    # patient_details = models.ForeignKey(Patient_Details, on_delete='CASCADE', default='')
    Image_Upload = models.FileField(upload_to='Patient_reports/')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Image_Upload)


class Scripts(models.Model):
    api_url = models.URLField(default='')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.api_url


class AI_Usecase_Occurences(models.Model):
    time = models.DateTimeField(default=datetime.now(), blank=True)
    Image_Output_1 = models.FileField(default='')
    confidence = models.CharField(max_length=5, default='')
    heatmap = models.FileField(default='')
    # Image_Output_2 = models.FileField()
    # Image_Output_3 = models.FileField()
    # Image_Output_4 = models.FileField()
    # Image_Output_5 = models.FileField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Image_Output_1) + "-" + str(self.confidence)


class Location(models.Model):
    location = models.CharField(max_length=1000)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.location)


class Test_Pathology(models.Model):
    some_test = models.CharField(max_length=500)
    api_url = models.URLField()

    # patient = models.ForeignKey(Patient_Details, on_delete='CASCADE', default='')
    # user = models.ForeignKey(User,null=True, on_delete='CASCADE')

    def __str__(self):
        return str(self.some_test)


class Reports(models.Model):
    patient_details = models.ForeignKey(Patient_Details, on_delete=models.CASCADE)
    test = models.ForeignKey(Test_Pathology, on_delete=models.CASCADE, default='')
    image_output = models.ForeignKey(AI_Usecase_Occurences, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default='')
    description = models.CharField(max_length=1000)
    # image_output = models.CharField(max_length=2000)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.description)


class Test(models.Model):
    test = models.CharField(max_length=500, unique=True)

    # script = models.ForeignKey(Scripts, on_delete='CASCADE', null=True)

    def __str__(self):
        return str(self.test)


class Lab_Api(models.Model):
    test = models.ForeignKey(Test_Pathology, on_delete=models.CASCADE, default='')
    # api_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.test)


class Lab_Api_Scripts(models.Model):
    lab_api = models.ForeignKey(Lab_Api, on_delete=models.CASCADE)
    scripts = models.ForeignKey(Scripts, on_delete=models.CASCADE)
    lab_api_scripts_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.lab_api_scripts_name)


class Lab_Api_On_Image_Input(models.Model):
    lab_api = models.ForeignKey(Lab_Api, on_delete=models.CASCADE)
    image_input = models.ForeignKey(Image_Input, on_delete=models.CASCADE)
    lab_api_on_image_input_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.lab_api_on_image_input_name)
