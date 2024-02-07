from rest_framework import serializers
from .models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Category
        fields = ['title', 'slug', 'created_at']


class ArticleReadSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    

    class Meta:
        model = Article
        fields = ['id','title', 'category', 'created_at']

    def get_category(self, obj):
        slug_cat = obj.category
        try:
         cat = Category.objects.get(slug=slug_cat)
         serializer = CategorySerializer(cat)
         return serializer.data
        except :
            return None
    
    
class ArticleSerializer(serializers.ModelSerializer):


    class Meta:
        model = Article
        fields = ['id', 'title', 'category', 'created_at']

