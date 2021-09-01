from django.db import models
from datetime import datetime


# Create your models here.


class Clients(models.Model):
    date=datetime.now()
    client_name=models.CharField(max_length=225,default=None)
    created_at=models.CharField(max_length=225,default=date)
    update_at=models.CharField(max_length=225,default=date)
    created_by=models.CharField(max_length=225,default='Rahit')

    def __str__(self):
        return self.client_name

    class Meta:
        db_table='Clients'


class Projects(models.Model):
    date = datetime.now()
    project_name=models.CharField(max_length=225,unique=True)
    created_at=models.CharField(max_length=225,default=date)
    updated_by=models.CharField(max_length=225,default=date)
    created_by=models.CharField(max_length=225,default='Ganesh')
    client=models.ForeignKey(Clients,on_delete=models.CASCADE,related_name='projects')

    def __str__(self):
        return self.project_name

    class Meta:
        db_table='Projects'


class Users(models.Model):
    name=models.CharField(max_length=255,null=True)
    project=models.ForeignKey(Projects,on_delete=models.CASCADE,related_name='users')

    def __str__(self):
        return self.name

    class Meta:
        db_table='Users'

