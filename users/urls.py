from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, CodeViewSet, ResendCodeModelViewSet, ResetPasswordModelViewSet

router = DefaultRouter()

router.register('', RegisterViewSet)

urlpatterns = [
    path('confirm_code/', CodeViewSet.as_view(({'post': 'create'}))),
    path('resend_code/', ResendCodeModelViewSet.as_view(({'post': 'create'}))),
    path('reset_password/', ResetPasswordModelViewSet.as_view(({'post': 'create'}))),
]

urlpatterns += router.urls
