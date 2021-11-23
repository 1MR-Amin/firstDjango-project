from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.BooleanField()

    def __str__(self):
        if self.gender:
            return f"{self.first_name} {self.last_name} M"
        return f"{self.first_name} {self.last_name} F"


class Contact(models.Model):
    telephone = models.CharField(max_length=50 ,null=False)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        if self.email:
            return self.email
        return self.telephone
