from djongo import models

isMigrate =False

class Category(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=100,db_column="title")
    slug=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = isMigrate   
        
    def __str__(self) :
        return f"{self.title}{self._id}"

class Article(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=100, db_column="title")
    created_at = models.DateTimeField(auto_now_add=True)
    category =models.ForeignKey(Category, 
           on_delete=models.CASCADE,
           null=True
         )
    def __str__(self) :
        return f"{self.title}{self._id}"

class Tag(models.Model):
    title = models.CharField(max_length=100,db_column="title")
    slug=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)