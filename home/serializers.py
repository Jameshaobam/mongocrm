from rest_framework import serializers
from .models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Category
        fields = ['title', 'slug', 'created_at']


class ArticleReadSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField()
    

    class Meta:
        model = Article
        pk = '_id'
        fields = ['_id', 'title', 'category', 'created_at']

    # def get_category(self, obj):
    #     slug_cat = obj.category
    #     try:
    #     #  cat = Category.objects.filter(slug=slug_cat).first()
    #     #  serializer = CategorySerializer(cat)
    #      return slug_cat
    #     except :
    #         return None
    
    
from rest_framework import serializers
from .models import Article, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'created_at']

class ArticleSerializer(serializers.ModelSerializer):
    # category = serializers.DictField(child=serializers.CharField())

    class Meta:
        model = Article
        pk = '_id'
        fields = ['_id', 'title', 'category', 'created_at']
    def create(self, validated_data):
        category_slug = validated_data.pop('category')  # Get the category slug from validated data
        try:
            # Try to retrieve the Category instance using the provided slug
            category_instance = Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            # If no matching Category instance is found, create a new one
            category_instance = Category.objects.create(slug=category_slug)

        # Create the Article instance with the retrieved or created Category instance
        article = Article.objects.create(category=category_instance, **validated_data)
        return article
    # def update(self, instance, validated_data):
    #     category_data = validated_data.pop('category')
    #     category_instance, _ = Category.objects.get_or_create(**category_data)

    #     instance.title = validated_data.get('title', instance.title)
    #     instance.created_at = validated_data.get('created_at', instance.created_at)
    #     instance.category = category_instance

    #     instance.save()
    #     return instance
    