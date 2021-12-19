from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import serializers

class HelloApiView(APIView):
    """test api view"""

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to treditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to urls',
        ]
        response = {
            'message': "Hello",
            'an_apiview' : an_apiview
        }
        return Response(response)

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            reponse = {
                'message' : message
            }
            return Response(reponse)
        else:
            return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({
            'method' : 'PUT',
        })
    
    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({
            'method' : 'patch',
        })
    
    def delete(self, request, pk=None):
        """Handle deletion of an object"""
        return Response({
            'method' : 'delete',
        })


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    """Test api view set"""
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'User actions( list, create, retrieve, update, partial_update).',
            'Autometically maps to urls using Routers.',
            'Provides more fucntionality with less code.'
        ]
        return Response({
            'message': 'Hello',
            'a_viewset': a_viewset
        })
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """get request, we need to provide id explicitly in url, not in form"""
        """Handle getting an object by its id"""
        return Response({
            'http_method': 'GET'
        })
    
    def update(self, request, pk=None):
        """put request"""
        """Handle updating an object by its id"""
        return Response({
            'http_method': 'PUT'
        })

    def partial_update(self, request, pk=None):
        """patch request"""
        """Handle updating part of an object by its id"""
        return Response({
            'http_method': 'PATCH'
        })
        
    def destroy(self, request, pk=None):
        """delete request"""
        """Handle deletion of an object by its id"""
        return Response({
            'http_method': 'DELETE'
        })