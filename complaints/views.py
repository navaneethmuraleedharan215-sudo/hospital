from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from complaints.serializers import SignupSerializer,ComplaintSerializer
from complaints.models import Complaints
from rest_framework.authtoken.models import Token
from complaints.permissions import IsOwner

# Create your views here.
class Signupview(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=SignupSerializer(data=form_data)

        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            qs=User.objects.create_user(**cleaned_data)

            serializer_instance=SignupSerializer(qs)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class ComplaintListCreateView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    #authentication_classes=[authentication.TokenAuthentication]
    
    
    

    def get(self,request):
        instance=Complaints.objects.filter(user=request.user)
        serializer_instance=ComplaintSerializer(instance,many=True)
        return Response(data=serializer_instance.data)


    def post(self,request):
        form_data=request.data
        serializer_instance=ComplaintSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class ComplaintRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk=None):

        instance = get_object_or_404(Complaints,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance = ComplaintSerializer(instance)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        instance = get_object_or_404(Complaints,id=pk)

        self.check_object_permissions(request,instance)

        form_data = request.data

        serializer_instance = ComplaintSerializer(data= form_data, instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data= serializer_instance.data)

        else: 

            return Response(data= serializer_instance.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Complaints,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response(data={"message":f"the complaint with ID = {pk} is deleted "})

class FilterByComplaintTypePriorityStatusView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        complaint_type = request.query_params.get("complaint_type")

        priority = request.query_params.get("priority")

        status = request.query_params.get("status")

        instance = Complaints.objects.filter(user=request.user,complaint_type= complaint_type,priority=priority,status=status)

        serializer_instance = ComplaintSerializer(instance,many=True)

        return Response(data=serializer_instance.data)
