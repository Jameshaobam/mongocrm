from djongo import models

isMigrate =False

class Category(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=100,db_column="title")
    slug=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = isMigrate   

class Article(models.Model):
    title = models.CharField(max_length=100,db_column="title")
    created_at = models.DateTimeField(auto_now_add=True)
    category=models.SlugField(null=True)


class Tag(models.Model):
    title = models.CharField(max_length=100,db_column="title")
    slug=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)