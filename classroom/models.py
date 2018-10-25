# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime

# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=10, blank=True)

class Course(models.Model):
    CATEGORIES = (
        ( 'MATH', 'Mathematics'),
        ( 'SCI', 'Science'),
        ( 'COMP', 'COMPUTER'),
        ( 'ENG', 'English'),
        ( 'PHYC', 'Physics'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='studentcourse')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    course = models.CharField(max_length=30, choices=CATEGORIES)
    enroll_date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.course