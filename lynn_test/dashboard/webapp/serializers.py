from django.contrib.auth.models import User
from rest_framework import serializers





#class roadtrackerserializer

class MobileSerializer(serializers.ModelSerializer):
    
    #the required forms ,we reduce on reusing forms by using this meta class
    class Meta:
        model = User
        fields = ('username', 'email')

