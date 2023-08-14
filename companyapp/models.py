from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=30,null=True)
    email=models.EmailField(max_length=30,null=True)
    contact=models.CharField(max_length=15,null=True)
    age=models.IntegerField(default=0)
    address=models.TextField(max_length=300,null=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    postingdate=models.IntegerField()
    location=models.CharField(max_length=30,default='')
    offeredsalary=models.CharField(max_length=30)
    qualification=models.TextField(max_length=300,default='')
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)

    class Meta:
        db_table='account'
