from rest_framework import serializers

from features.cards.models import Card


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('id',
                  'front_text',
                  'back_text',
                  'created_at',
                  'updated_at')
