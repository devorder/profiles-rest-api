from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test api view"""
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
