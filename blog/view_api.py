from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .helper import *
from django.contrib.auth import authenticate , login

class LoginView(APIView):
    
    def post(self , request):
        response = {}
        response['status'] = 500
        try:
            data = request.data
                        
            check_user = User.objects.filter(username = data.get('username')).first()
            
            if check_user is None:
                response['message'] = 'Invalid Email , user not found'
                raise Exception('Invalid Email not found')
            
            user_obj = authenticate(username = data.get('username') , password = data.get('password'))
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                #response['message'] = 'Welcome'
            else:
                response['message'] = 'Invalid password'
                raise Exception('Invalid password')
             
        except Exception as e :
            print(e)
            
        return Response(response)
            
  
LoginView = LoginView.as_view()




class RegisterView(APIView):
    
    def post(self , request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data          
            
            check_user = User.objects.filter(email = data.get('email')).first()
            
            if check_user:
                response['message'] = 'Email already taken'
                raise Exception('Email already taken')

            user_obj = User.objects.create(username = data.get('email'), email = data.get('email'), first_name = data.get('first_name'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['message'] = 'User created '
            response['status'] = 200
           
        except Exception as e :
            print(e)
            
        return Response(response)
            
                
RegisterView = RegisterView.as_view()