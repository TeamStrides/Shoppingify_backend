from django.shortcuts import render
from django.http import JsonResponse

def testing (request, *args, **kwargs):
    return JsonResponse({
        'status' : 200,
        'message' : "Testing is succesful"
    })
