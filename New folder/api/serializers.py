
from rest_framework import serializers
from api.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'programming_language',
                  'developer_role', 'userid', 'date_employed', 'photo')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    records = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name',
                  'last_name', 'password', 'records')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        records_data = validated_data.pop('records')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **records_data)
        return user

    def update(self, instance, validated_data):
        records_data = validated_data.pop('records')
        records = instance.records

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        records.id = records_data.get('id', records.id)
        records.first_name = records_data.get('first_name', records.first_name)
        records.last_name = records_data.get('last_name', records.last_name)
        records.date_employed = records_data.get(
            'date_employed', records.date_employed)
        records.programming_language = records_data.get(
            'programming_language', records.programming_language)
        records.developer_role = records_data.get(
            'developer_role', records.developer_role)
        records.userid = records_data.get('userid', records.userid)
        records.photo = records_data.get('photo', records.photo)
        records.save()

        return instance
