from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login
from apiRegistroLogin.serializers import UserSerializer


class LoginView(APIView):
   def post(self, request):
       serializer = UserSerializer(data=request.data)

       if serializer.is_valid():
           username = serializer.validated_data['username']
           password = serializer.validated_data['password']

           user = authenticate(request, username=username, password=password)

           if user is not None:
               login(request, user)

               return Response({'message': 'Inicio de sesión exitoso'})

           else:
               return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)

       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
