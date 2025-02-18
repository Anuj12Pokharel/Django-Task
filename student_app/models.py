from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.TextField()
    grade = models.CharField(max_length=10)
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.name

