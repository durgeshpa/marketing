from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from .models import TokenModel
from rest_framework import status
from rest_framework.decorators import api_view
import json
@api_view(['GET','POST','PATCH'])
def handle_redirect_uri(request):
    """
    Callback view for handling redirect URI after user authorization.

    Args:
    request: The HttpRequest object.

    Returns:
    A Django HttpResponse object.
    """
    print(f"{request.method}")
    try:
        access_token = request.GET.get("code")
        print("\n\n==============================================\n\n")
        #req = json.dump(request.__dict__)
        print("\n\n==============================================\n\n")

        TokenModel.objects.create(token=access_token,request={})
        data = TokenModel.objects.all().values()
    except Exception as e:
        print(e)
        data = TokenModel.objects.all().values()

    # Redirect to your application's main page or desired location
    return Response({"msg":"sucess","data":data})