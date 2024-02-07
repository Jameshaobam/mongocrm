
from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.articles ,name="articles"),
      path('create/',views.create_article, name='create_article'),
       path('delete/<str:id>',views.delete_article, name='delete_article'),
    
]