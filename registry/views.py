from django.contrib.auth.hashers import check_password
from rest_framework.viewsets import ModelViewSet
from .serializers import User, UserSerializer
from .permissions import BaseUserPermission
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


def getUserLoginData(request):
    cpf = request.data.get('cpf', '')
    email = request.data.get('email', '')
    pis = request.data.get('pis', '')
    password = request.data.get('password', '')
    return {
        'cpf': cpf,
        'email': email,
        'pis': pis,
        'password': password
    }


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [BaseUserPermission, ]

    @action(detail=False, methods=['GET'], url_path='byUsername/(?P<username>\w+)')
    def getUserByUsername(self, request, username, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
            serialized = UserSerializer(user)
            returnData = serialized.data
            returnStatus = status.HTTP_200_OK
        except:
            returnData = {'error': 'User not found'}
            returnStatus = status.HTTP_404_NOT_FOUND
        return Response(returnData, returnStatus)

    @action(detail=False, methods=['post', ])
    def getUserLogin(self, request, *args, **kwargs):
        using = request.data.get('using', '')
        loginsData = getUserLoginData(request)

        usingValue = loginsData.get(using, '')
        userLoginDict = dict()
        if using != 'email':
            userLoginDict[f'profile__{using}'] = usingValue
        else:
            userLoginDict['email'] = usingValue

        return_dict = dict()
        return_status = status.HTTP_200_OK
        if loginsData.get(using, None) is not None:
            try:
                correctUser = None
                users = User.objects.filter(**userLoginDict)
                for user in users:
                    if check_password(loginsData['password'], user.password):
                        correctUser = UserSerializer(user)
                        break

                if correctUser:
                    return_dict = correctUser.data
                else:
                    return_dict['error'] = 'No user found!'
                    return_status = status.HTTP_404_NOT_FOUND
            except Exception as err:
                return_dict['error'] = str(err)
                return_status = status.HTTP_404_NOT_FOUND
        return Response(return_dict, status=return_status)
