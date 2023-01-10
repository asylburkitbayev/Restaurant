from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import User
from .serializers import RegistrationSerializer, CodeSerializer, ResendCodeSerializer, ResetPasswordSerializer
from .utils import send_verification_mail, generate_activation_code


class RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class CodeViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = serializer.validated_data['code']
            check_user = User.objects.filter(email=email).exists()
            if check_user:
                user = User.objects.get(email=email)
                if user.code == code:
                    user.is_active = True
                    user.save()
                    return Response({
                        'message': 'Код успешно активирован!'
                    }, status=status.HTTP_201_CREATED)
                return Response({'message': 'Неверный код'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': f'Пользователь с почтой {email} не найден'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResendCodeModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ResendCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = ResendCodeSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = generate_activation_code()
            check_user = User.objects.get(email=email)
            if check_user:
                check_user.code = code
                check_user.save()
                send_verification_mail(check_user.email, check_user.code)

                return Response({
                    'id': check_user.pk,
                    'code': check_user.code,
                    'message': 'Код отправлен успешно'
                }, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            check_user = User.objects.get(email=email)
            if check_user:
                check_user.password = password
                check_user.set_password(password)
                check_user.save()

                return Response({'message': 'Пароль успешно изменен'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
