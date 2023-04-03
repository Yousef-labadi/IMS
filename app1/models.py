from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) <= 0:
            errors["first_name"] = "Must enter a first name!"
        elif len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters!"
        if len(postData['last_name']) <= 0:
            errors["last_name"] = "Must enter a last name!"
        elif len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters!"
        if len(postData['pwd']) <= 0:
            errors["pwd"] = "Password is required!"
        if len(postData['pwd']) < 8:
            errors['pwd'] = "Password must be at least 8 characters!"
        EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="invalid email address!"
        if len(postData['email']) <= 0:
            errors["email"] = "Email is required!"
        if User.objects.filter(email = postData['email']).exists():
            errors['email'] = "Email already exists."
    
        if postData['cpwd'] != postData['pwd']:
            errors['cpwd'] = "Confirmation password does not match password!"
        return errors
    
    def log_validation(self, postData):
        errors = {}
        try:
            user = User.objects.get(email = postData['email'])
        except:
            errors['email'] = "Invalid Inputs"
            return errors
        if not bcrypt.checkpw(postData['pwd'].encode(), user.password.encode()):
            errors['pwd'] = "Invalid Inputs"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Product(models.Model):
    name=models.TextField()
    category=models.TextField()
    price=models.FloatField()
    quantity=models.FloatField()
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    






# Create your models here.
