from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import product
import json
@csrf_exempt
def products(request):
# GET ALL EMPLOYEES
    if request.method == "GET":
        data = list(product.objects.values())
        return JsonResponse(data, safe=False)
# CREATE EMPLOYEE
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        product.objects.create(
            name=body["name"],
            type=body["type"],
            price=body["price"]
        )
        return JsonResponse({"message": "POST EXECUTED"})
# UPDATE EMPLOYEE (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        pro = product.objects.get(id=body["id"])
        pro.name = body["name"]
        pro.type = body["type"]
        pro.price = body["price"]

        pro.save()
        return JsonResponse({"message": "PUT EXECUTED"})
# DELETE EMPLOYEE (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        pro = product.objects.get(id=body["id"])
        pro.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})
    return JsonResponse({"error": "Method not allowed"}, status=405)