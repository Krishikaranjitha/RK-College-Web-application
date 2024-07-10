from django.db import models

from django.db import models
import os
import datetime

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

    
class St_results(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer science and Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('ECE', 'Electronics and communication Engineering'),
        ('CE', 'Civil Engineering'),
        ('ME', 'Mechanical Engineering'),
    ]
    
    Name=models.CharField(max_length=20,null=False,blank=False)
    DOB = models.DateField(null=False,blank=False)
    Age=models.IntegerField(null=False,blank=False)
    Reg_number=models.CharField(max_length=20,unique=True,null=False,blank=False)
    Department=models.CharField(max_length=255,choices=DEPARTMENT_CHOICES)
    Tamil=models.IntegerField(default=0)
    English=models.IntegerField(default=0)
    Maths=models.IntegerField(default=0)
    Physics=models.IntegerField(default=0)
    Chemistry=models.IntegerField(default=0)
    Biology=models.IntegerField(default=0)
    Total=models.IntegerField(default=0,editable=False)
    Average=models.FloatField(default=0.0,editable=False)
    status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    
    def save(self, *args, **kwargs):
        self.Total = self.Tamil + self.English + self.Maths + self.Chemistry + self.Physics + self.Biology
        self.Average = self.Total / 6
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.Name+" "+f"{self.Reg_number}"+" "+f"{self.DOB}"
    


class St_Registration(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer science and Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('ECE', 'Electronics and communication Engineering'),
        ('CE', 'Civil Engineering'),
        ('ME', 'Mechanical Engineering'),
    ]
    
    BLOOD_GROUP=[
        ('B+ve','B+ve'),
        ('A+ve','A+ve'),
        ('AB+ve','AB+ve'),
        ('AB-ve','AB-ve'),
        ('A-ve','A-ve'),
        ('B-ve','B-ve'),
        ('O+ve','O-ve'),
        
    ]
    Name=models.CharField(max_length=20,null=False,blank=False)
    Fathers_name=models.CharField(max_length=20,null=True,blank=True)
    DOB = models.DateField(null=False,blank=False)
    Age=models.IntegerField(null=False,blank=False)
    Address=models.TextField(max_length=500,null=True,blank=True)
    Department=models.CharField(max_length=255,choices=DEPARTMENT_CHOICES)
    Reg_number=models.CharField(max_length=20,unique=True,null=False,blank=False)
    Gender=models.CharField(max_length=50,choices=[('Male','Male'),('Female','Female'),('Others','Others')])
    Blood_Group=models.CharField(max_length=50,choices=BLOOD_GROUP,null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='uploads/')
    status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    Tamil=models.IntegerField(default=0)
    English=models.IntegerField(default=0)
    Maths=models.IntegerField(default=0)
    Physics=models.IntegerField(default=0)
    Chemistry=models.IntegerField(default=0)
    Fundamentals_of_engg=models.IntegerField(default=0)
    Total=models.IntegerField(default=0,editable=False)
    Average=models.FloatField(default=0.0,editable=False)

    
    def save(self, *args, **kwargs):
        self.Total = self.Tamil + self.English + self.Maths + self.Chemistry + self.Physics + self.Fundamentals_of_engg
        self.Average = self.Total / 6
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.Name+" "+f"{self.Reg_number}"+" "+f"{self.DOB}"
    
class Col_Fees(models.Model):
    Details=models.CharField(max_length=255)
    Fees=models.FloatField()
        
    def __str__(self):
        return self.Details
        
        
class Hos_Fees(models.Model):
    Details=models.CharField(max_length=255)
    Fees=models.FloatField()
        
    def __str__(self):
            return self.Details
        
        
class gallery(models.Model):    
    image=models.ImageField(null=True,blank=True,upload_to='uploads/')

        
