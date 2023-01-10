from rest_framework import serializers
from .models import User
from .utils import generate_activation_code, send_verification_mail


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}
                                     )

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'phone', 'password', 'is_active']

        extra_kwargs = {
            # 'password': {'write_only': True},
            'email': {'required': True},
            'is_active': {'read_only': True}
        }

    def create(self, validated_data):
        code = generate_activation_code()
        user = User(
            email=validated_data['email'],
            phone=validated_data['phone'],
            username=validated_data['username'],
            code=code,
        )
        user.set_password(validated_data['password'])
        user.save()
        send_verification_mail(user.email, user.code)
        return user


class CodeSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    email = serializers.EmailField()


class ResendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}
                                     )
