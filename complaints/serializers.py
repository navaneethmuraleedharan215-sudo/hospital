from rest_framework import serializers
from django.contrib.auth.models import User
from complaints.models import Complaints



class SignupSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","first_name","last_name","email","password"]

        read_only_fields =["id"]


class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:

        model = Complaints

        fields ="__all__"

        read_only_fields = ["id","user","reported_date","status"]
      