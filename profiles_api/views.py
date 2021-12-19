from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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