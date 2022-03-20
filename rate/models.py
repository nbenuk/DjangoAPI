from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Professor(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    def __str__(self):
            return self.name
class Module(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ModuleInstance(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    year = models.DateField(default=timezone.now)

    semester = models.IntegerField(        
        validators=[MaxValueValidator(2), MinValueValidator(1)])
    professor = models.ManyToManyField(Professor)
    def __str__(self):
        return self.module.name

class Rating(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(ModuleInstance, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    def __str__(self):
        return self.module.module.name


