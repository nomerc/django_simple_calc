from api.models import Operation
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import OperationSerializer, ArgAndOpSerializer
from rest_framework.parsers import JSONParser

# Create your views here.


def main(request):
    return HttpResponse("Hello")


class CalcView(APIView):

    def get(self, request, format=None):
        # lastOp = Operation.objects.order_by('-performed')[0]
        # return Response(OperationSerializer(lastOp).data, status=status.HTTP_200_OK)
        operations = Operation.objects.all()
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = ArgAndOpSerializer(data=data)
        if(serializer.is_valid()):
            arg1 = serializer.data['arg1']
            arg2 = serializer.data['arg2']
            op = serializer.data['operation_name']

            if(op == '+'):
                result = arg1 + arg2
            else:
                if(op == '-'):
                    result = arg1 - arg2
                else:
                    result = arg1 * arg2

            operation = Operation(arg1=arg1, arg2=arg2,
                                  operation_name=op, result=result)
            operation.save()

            return Response(OperationSerializer(operation).data, status=status.HTTP_200_OK)
        else:
            return Response(data=None, status=status.HTTP_406_NOT_ACCEPTABLE)
