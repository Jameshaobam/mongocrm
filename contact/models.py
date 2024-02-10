from django.db import models

# Create your models here.
class Contact(models.Model):
    context = models.CharField(max_length=100,db_column="context")
    email=models.CharField(max_length=100,db_column="email")
    
    def __str__(self):
        
        return f"{self.id}"