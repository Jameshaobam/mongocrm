from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer

@api_view(['POST'])
def create_contact(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the instance without specifying the database
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def list_contacts(request):
    if request.method == 'GET':
        contacts = Contact.objects.using('test_db').all()  # Fetch contacts from the test_db
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)