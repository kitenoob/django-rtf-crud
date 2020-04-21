from rest_framework import serializers
from api.models import User, Object


#class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = '__all__'

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class ObjectSerializer(serializers.ModelSerializer):
    
    # to get owner name instead of id
    #owner = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Object
        fields = ['id', 'name', 'owner', 'created']
        #depth = 1 # to get owner object instead of id