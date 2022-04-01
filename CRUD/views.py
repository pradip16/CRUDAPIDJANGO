from shutil import ExecError
from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import Crud_opr
# Create your views here.
def index(request):
    return render(request,"apicall.html")


def add_data(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if name=="" or email=="" or password=="":
            payload = {
                "data":"",
                "status":"Empty data not valid"
            }
            return HttpResponse(json.dumps({"status_code":400,"payload":payload}),content_type="aplication/json")

        elif str(email).endswith("@gmail.com") == False:
            payload = {
                "data":"",
                "status":"Email not valid"
            }
            return HttpResponse(json.dumps({"status_code":400,"payload":payload}),content_type="aplication/json")

        else:
            try:
                add_data = Crud_opr(Name=name,Email=email,Password=password)
                add_data.save()
                data = Crud_opr.objects.all()
                data_lst = []
                for i in data:
                    d1 = {
                        "id":i.pk,
                        "name":i.Name,
                        "email":i.Email,
                        "password":i.Password
                    }
                    data_lst.append(d1)
                payload = {
                    "data":data_lst,
                    "status":"Data added successfully done."
                }
                return HttpResponse(json.dumps({"status":200,"payload":payload}),content_type="aplication/json")
            except Exception as e:
                payload = {
                    "data":"",
                    "status":str(e)
                }
                return HttpResponse(json.dumps({"status":200,"payload":payload}),content_type="aplication/json")
    else:
        payload={
            "data":"",
            "status":"Method not allow"
        }
        return HttpResponse(json.dumps({"status_code":400,"payload":payload}),content_type="aplication/json")        


def delete_data(request):
    if request.method == "POST":
        try:
            id =request.POST.get("id")
            # print(id)
            Crud_opr.objects.get(pk=id).delete()
            data = Crud_opr.objects.all()
            data_lst = []
            for i in data:
                d1 = {
                    "id":i.pk,
                    "name":i.Name,
                    "email":i.Email,
                    "password":i.Password
                }
                data_lst.append(d1)
            payload={
                "data":data_lst,
                "status":"Data deleted successfully done."
            }
            return HttpResponse(json.dumps({"status_code":200,"payload":payload}),content_type="aplication/json")
        except Exception as e:
            payload={
                "data":"",
                "status":str(e)
            }
            return HttpResponse(json.dumps({"status_code":400,"payload":payload}),content_type="aplication/json")

    else:
        payload={
            "data":"",
            "status":"Method not allow"
        }
        return HttpResponse(json.dumps({"status_code":400,"payload":payload}),content_type="aplication/json")


def update_data(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if name=="" or email=="" or password=="":
            payload = {
                "data":"",
                "status":"Empty data not valid"
            }
            return HttpResponse(json.dumps({"status_code":400,"payload":payload}),content_type="aplication/json")

        elif str(email).endswith("@gmail.com") == False:
            payload = {
                "data":"",
                "status":"Email not valid"
            }
            return HttpResponse(json.dumps({"status_code":400,"payload":payload}),content_type="aplication/json")

        else:
            try:
                add_data = Crud_opr.objects.get(pk=id)
                add_data.Name=name
                add_data.Email=email
                add_data.Password=password

                add_data.save()
                data = Crud_opr.objects.all()
                data_lst = []
                for i in data:
                    d1 = {
                        "id":i.pk,
                        "name":i.Name,
                        "email":i.Email,
                        "password":i.Password
                    }
                    data_lst.append(d1)
                payload = {
                    "data":data_lst,
                    "status":"Data updated successfully done."
                }
                return HttpResponse(json.dumps({"status":200,"payload":payload}),content_type="aplication/json")
            except Exception as e:
                payload = {
                    "data":"",
                    "status":str(e)
                }
                return HttpResponse(json.dumps({"status":200,"payload":payload}),content_type="aplication/json")
    else:
        payload={
            "data":"",
            "status":"Method not allow"
        }
        return HttpResponse(json.dumps({"status_code":400,"payload":payload}),content_type="aplication/json")        





#API Slugs

##### -----------------------------------------------------
#### --- add_data
## url == http://127.0.0.1:8000/add_data/

## method == POST

## slug
# name =
# email=
# password

## Response
# {
#     "status": 200,
#     "payload": {
#         "data": [
#             {
#                 "id": 1,
#                 "name": "pradip",
#                 "email": "pradip@gmail.com",
#                 "password": "pradip12345678"
#             },
#             {
#                 "id": 2,
#                 "name": "pradip",
#                 "email": "pradip@gmail.com",
#                 "password": "pradip12345678"
#             },
#             {
#                 "id": 3,
#                 "name": "roshan",
#                 "email": "roshan@gmail.com",
#                 "password": "rohan1234567"
#             }
#         ],
#         "status": "Data added successfully done."
#     }
# }
##### -----------------------------------------------------



##### -----------------------------------------------------
#### --- delete_data
## url == http://127.0.0.1:8000/delete_data/

## method == POST

## slug
# id =2

## Response
# {
#     "status": 200,
#     "payload": {
#         "data": [
#             {
#                 "id": 1,
#                 "name": "pradip",
#                 "email": "pradip@gmail.com",
#                 "password": "pradip12345678"
#             },
#             {
#                 "id": 3,
#                 "name": "roshan",
#                 "email": "roshan@gmail.com",
#                 "password": "rohan1234567"
#             }
#         ],
#         "status": "Data deleted successfully done."
#     }
# }
##### -----------------------------------------------------





##### -----------------------------------------------------
#### --- update_data
## url == http://127.0.0.1:8000/update_data/

## method == POST

## slug
# id = 1
# name =
# email=
# password

## Response
# {
#     "status": 200,
#     "payload": {
#         "data": [
#             {
#                 "id": 1,
#                 "name": "sdfghjk",
#                 "email": "asdfgh@gmail.com",
#                 "password": "asdfghjk"
#             },
#             {
#                 "id": 3,
#                 "name": "roshan",
#                 "email": "roshan@gmail.com",
#                 "password": "rohan1234567"
#             }
#         ],
#         "status": "Data updated successfully done."
#     }
# }
##### -----------------------------------------------------