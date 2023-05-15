from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        #fields = ('title', 'text',)

#class RandomViewSet(serializers.Serializer):
#    name = serializers.CharField()
#    surname = serializers.CharField()