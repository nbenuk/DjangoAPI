from ast import Mod
from rest_framework import serializers
from .models import Module, ModuleInstance, Professor, Rating
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username','password' , 'email']
class UserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

class ModuleInstanceSerializer(serializers.ModelSerializer):
    professor = serializers.SlugRelatedField(
            many=True,
            read_only=True,
            slug_field="name"
        )
    # module = serializers.SlugRelatedField(
    #         many=False,
    #         read_only=True,
    #         slug_field="name"
    #     )
    module = serializers.SlugRelatedField(
            many=False,
            read_only=True,
            slug_field="code"
        )

    class Meta:
        model = ModuleInstance
        fields = ('module', 'professor', 'year', 'semester')


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

# class InputSerializer(serializers.)

class RatingSerializer(serializers.ModelSerializer):
    professor = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all())
    module = serializers.PrimaryKeyRelatedField(queryset=ModuleInstance.objects.all())

    class Meta:
        model = Rating
        fields = '__all__'
        # fields = ['username','code','rating','professor' ]

        