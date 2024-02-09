from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


from .models import Article
from .serializers import ArticleSerializer,ArticleReadSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def articles(req):
    try:
       articles =   Article.objects.all()
       
       serializer =  ArticleReadSerializer(articles,many=True)
       
       return Response({
           "status":200,
           "detail":"success",
           "data":serializer.data
       },status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            "status":500,
            "detail":f"{e}"
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        

@api_view(['POST'])
def create_article(request):
    if request.method == 'POST':
        
        
        
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
@api_view(['DELETE'])     
def delete_article(req,id):
    try:
        article =  Article.objects.get(id=id)
        article.delete()
        return Response({"status":200,
                         "detail":f"{id} deleted"
                         }, status=status.HTTP_200_OK)
    
    except Exception as e:
                return Response({
            "status":500,
            "detail":f"{e}"
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        