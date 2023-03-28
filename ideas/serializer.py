from .models import Idea, Vote
from rest_framework import serializers


class IdeaSerializer(serializers.HyperlinkedModelSerializer):  #klasa MODUL+serializer
    class Meta:
        model = Idea
        fields = ['id', 'title', 'description', 'youtube_url', 'status']




class VoteSerializer(serializers.HyperlinkedModelSerializer):  #klasa MODUL+serializer
    class Meta:
        model = Vote
        fields = ['idea', 'reason']

