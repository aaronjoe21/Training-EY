from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vehicle
import json
@csrf_exempt
def vehicle(request):
# GET ALL EMPLOYEES
    if request.method == "GET":
        data = list(Vehicle.objects.values())
        return JsonResponse(data, safe=False)
# CREATE EMPLOYEE
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        Vehicle.objects.create(
            number_plate=body["number_plate"],
            vehicle_type=body["vehicle_type"],
            manufacturer=body["vehicle_type"],
            year=body["year"]
        )
        return JsonResponse({"message": "POST EXECUTED"})
# UPDATE EMPLOYEE (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        pro = Vehicle.objects.get(id=body["id"])
        pro.number_plate = body["number_plate"],
        pro.vehicle_type = body["vehicle_type"],
        pro.manufacturer = body["vehicle_type"],
        pro.year = body["year"]

        pro.save()
        return JsonResponse({"message": "PUT EXECUTED"})
# DELETE EMPLOYEE (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        pro = Vehicle.objects.get(id=body["id"])
        pro.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})
    return JsonResponse({"error": "Method not allowed"}, status=405)