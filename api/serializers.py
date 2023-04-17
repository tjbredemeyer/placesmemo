'''
Serializers allow complex data such as querysets and model instances 
to be converted to native Python datatypes that can then be easily 
rendered into JSON, XML or other content types. Serializers also provide 
deserialization, allowing parsed data to be converted back into complex 
types, after first validating the incoming data.
'''
from rest_framework import serializers
from places.models import Place, Tag


class TagSerializer(serializers.ModelSerializer):
    '''This class represents the serializer for the Tag model.'''

    places = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        '''This class represents the meta class for the TagSerializer.'''
        model = Tag
        fields = '__all__'


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    '''This class represents the serializer for the Place model.'''

    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )

    class Meta:
        '''This class represents the meta class for the PlaceSerializer.'''
        model = Place
        fields = (
            'name', 
            'rating', 
            'notes', 
            'tags', 
            'yelp_id', 
            'location'
            )
