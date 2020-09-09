from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import CustomUser
from .serializer import UserCreateSerializer
from django.db.models import signals
from django.conf import settings
from rest_framework.authtoken.models import Token


@api_view(['Get'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    print(request.user)
    print(request.auth)
    return Response(data="only for logged in user", status=status.HTTP_200_OK)


class RegistrationView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user)
        signals.post_save.send(sender=self.__class__, user=user, request=self.request)
        headers = self.get_success_headers(serializer.data)

        # 1st Way of creating token
        # token = Token.objects.create(user=user)
        #print(token.key)

        # 2nd way of creating token that is cleaner
        signals.post_save.send(sender=self.__class__, user=user, request=self.request)

        # then we query the token for this specific user that was returned by the serializer
        token = Token.objects.get(user=user).key
        print(token)

        return Response(data=token, status=status.HTTP_201_CREATED, headers=headers)
