from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    date_of_birth = models.DateField(name="date_of_birth", null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.username}"


class Goal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    calories = models.IntegerField(null=False)
    protein = models.IntegerField(null=False)
    carbohydrate = models.IntegerField(null=False)
    fats = models.IntegerField(null=False)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)

    def __str__(self):
        return f"{self.user} goal is: /n, calories:{self.calories} /n, protein:{self.protein} /n, carbohydrate:{self.carbohydrate} /n, fats:{self.fats}"



