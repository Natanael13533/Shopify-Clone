from typing import List
from ninja import NinjaAPI, Query

from ninja_simple_jwt.auth.views.api import mobile_auth_router
from ninja_simple_jwt.auth.ninja_auth import HttpJwtAuth

from django.contrib.auth.models import User
from customer.models import Customer, Address

from customer.schemas import CustomerRespon, AddressIn, AddressRespon


api = NinjaAPI()
api.add_router("/auth/", mobile_auth_router)
apiAuth = HttpJwtAuth()

@api.get("hello")
def helloWorld(request):
    return {"Hello": "World"}

@api.get("customers.json", auth=apiAuth, response=CustomerRespon)
def getAllCustomer(request, ids:str):
    int_ids = ids.split(',')
    customers = Customer.objects.filter(id__in=int_ids)
    return {"customers": customers}

@api.post("customers/{id_cust}/addresses.json", auth=apiAuth, response=AddressRespon)
def addCustomer(request, id_cust:int, data:AddressIn):
    customer = Customer.objects.get(pk=id_cust)
    user = customer.user
    user.first_name = data.first_name
    user.last_name = data.last_name
    user.save()

    newAddress = Address.objects.create(customer=customer,
                           address1=data.address1,
                           address2=data.address2,
                           city=data.city,
                           province=data.province,
                           company=data.company,
                           phone=data.phone,
                           zip=data.zip,
                           default=data.default)
    
    return {"customer_address": [newAddress]}

@api.put("customers/{id_cust}/addresses/{id_address}/default.json", auth=apiAuth, response=AddressRespon)
def setDefaultAddress(request, id_cust:int, id_address:int):
    address = Address.objects.get(pk=id_address)
    address.default=True
    address.save()

    other = Address.objects.filter(customer_id=id_cust).exclude(id=id_address)
    for data in other:
        data.default=False
        data.save()
    
    return {"customer_address": [address]}

@api.delete("customers/{id_cust}/addresses/{id_address}.json")
def deleteAddress(request, id_cust:int, id_address:int):
    address = Address.objects.get(pk=id_address)
    address.delete()

    return {}