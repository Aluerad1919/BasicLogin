from django.db import models
import re
from datetime import datetime, timedelta
class Darth_Valid(models.Manager):
    def count_Vald(self, postData):
        errors = {}
        dob = postData['bday_input']
        dob_obj = datetime.strptime(dob,'%Y-%m-%d')
        today = datetime.today()
        min_year = today - timedelta(days=4745)
        if len(Users.objects.filter(email=postData['email_input'])) > 0:
            errors['email_input'] = 'POPE OF NOPE!!! Ye shall be Smitted...Smittened..smotted... bad things will befall you.'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_input']):
            errors['email_input'] = "Invalid email address!"
        if len(postData['first_name_input']) < 2:
            errors['first_name_input'] = 'First name must be more than 2 characters long'
        if len(postData['last_name_input']) < 2:
            errors['last_name_input'] = 'Last name must be more than 2 characters long'
        if len(postData['pw_input']) < 8:
            errors['pw_input'] = 'Dipshit, you need 8Chars min!!!'
        if postData['pw_input'] != postData['confirm_input']:
            errors['pw_input'] = 'Passwords do not match.'
        print(dob_obj,today,dob,min_year)
        if  dob_obj > today:
            errors['bday_input'] = 'How do you exist? Are you a time traveler? Send winning lotto numbers to Dev Team for equal share!!!'
        if  dob_obj > min_year and dob < today:
            errors['bday_input'] = 'Not Old enough'
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    email = models.EmailField()
    birthdate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Darth_Valid()