from typing import List
from ninja import Router
from django.http import HttpResponse

from django.contrib.auth.models import User
from customer.models import Customer, Address

from customer.schemas import CustomerIn, CustomerInUpdate, CustomerRespon, AddressIn, AddressRespon, AddressesRespon, SingleCustomerRespon, parse_query, CountCustomer

from typing import Optional

router = Router()

@router.get("hello")
def helloWorld(request):
    return {"Hello": "World"}

# CUSTOMER

@router.post("customers.json", response=SingleCustomerRespon)
def addCustomer(request, data:CustomerIn):
    user = User.objects.create_user(username=data.email,
                                    email=data.email,
                                    first_name=data.first_name,
                                    last_name=data.last_name,
                                    password=None)

    newCustomer = Customer.objects.create(user=user,
                                          state=data.state,
                                          verified_email=data.verified_email,
                                          send_email_welcome=data.send_email_welcome,
                                          currency=data.currency,
                                          phone=data.phone)
    
    if data.addresses:
        for address_data in data.addresses:
            address = Address.objects.create(
                customer=newCustomer,
                address1=address_data.address1,
                address2=address_data.address2,
                city=address_data.city,
                province=address_data.province,
                country=address_data.country,
                phone=address_data.phone,
                zip=address_data.zip,
                company=address_data.company,
                default=address_data.default or False
            )
            newCustomer.address_set.add(address)
    
    return {"customer": newCustomer}

@router.put("customers/{id_cust}.json", response=SingleCustomerRespon)
def updateCustomer(request, id_cust:int, data:CustomerInUpdate):

    try:
        # Retrieve existing customer
        customer = Customer.objects.get(pk=id_cust)

        user = customer.user
        user.email = data.email
        user.first_name = data.first_name
        user.last_name = data.last_name
        user.save()

        customer.state = data.state
        customer.verified_email = data.verified_email
        customer.send_email_welcome = data.send_email_welcome
        customer.currency = data.currency
        customer.phone = data.phone
        customer.save()
    
    except:
        return HttpResponse("Customer not found", status=404)
    
    return {"customer": customer}

@router.get("customers.json", response=CustomerRespon)
def getAllCustomer(request, ids:str):
    int_ids = ids.split(',')
    customers = Customer.objects.filter(id__in=int_ids)
    
    return {"customers": customers}

@router.get("customers/{id_cust}.json", response=SingleCustomerRespon)
def getSingleCustomer(request, id_cust:str):
    customer = Customer.objects.get(pk=id_cust)
    
    return {"customer": customer}

@router.get("customers/count/count.json", response=CountCustomer)
def count_customers(request):
    customer_count = Customer.objects.count()
    
    return {"count": customer_count}

@router.get("customers/query/search.json", response=CustomerRespon)
def getQueryCustomer(request, query: str):
    customers = Customer.objects.all()
    filters = parse_query(query)

    if 'id' in filters:
        customers = Customer.objects.filter(pk=filters['id'])
    if 'email' in filters:
        customers = Customer.objects.filter(user__email=filters['email'])
    if 'first_name' in filters:
        customers = Customer.objects.filter(user__first_name=filters['first_name'])
    if 'last_name' in filters:
        customers = Customer.objects.filter(user__last_name=filters['last_name'])
    if 'city' in filters:
        customers = Customer.objects.filter(address_set__city__icontains=filters['city'])
    if 'state' in filters:
        customers = Customer.objects.filter(state__icontains=filters['state'])
    if 'country' in filters:
        customers = Customer.objects.filter(address_set__country__icontains=filters['country'])
    if 'address1' in filters:
        customers = Customer.objects.filter(address_set__address1__icontains=filters['address1'])
    if 'address2' in filters:
        customers = Customer.objects.filter(address_set__address2__icontains=filters['address2'])
    if 'company' in filters:
        customers = Customer.objects.filter(address_set__company__icontains=filters['company'])
    if 'verified_email' in filters:
        customers = Customer.objects.filter(verified_email__icontains=filters['verified_email'])
    if 'phone' in filters:
        customers = Customer.objects.filter(phone__icontains=filters['phone'])
    if 'updated_at' in filters:
        customers = Customer.objects.filter(updated_at__icontains=filters['updated_at'])

    return {"customers": customers}

@router.delete("customers/{id_cust}.json")
def deleteCustomer(request, id_cust:int):
    try:
        customer = Customer.objects.get(pk=id_cust)

        addresses = Address.objects.filter(customer=customer)
        addresses.delete()

        customer.delete()

        return {}

    except:
        return HttpResponse("Customer not found", status=404)


# ADDRESS

@router.get("customers/{id_cust}/addresses.json", response=AddressesRespon)
def getAllAddresses(request, id_cust:int, limit: Optional[int] = None):
    customer = Customer.objects.get(pk=id_cust)

    addresses = Address.objects.filter(customer=customer)

    if limit:
        addresses = addresses[:limit]
    
    return {"addresses": addresses}

@router.get("customers/{id_cust}/addresses/{id_address}.json", response=AddressRespon)
def getSingleAddressCustomer(request, id_cust:int, id_address:int):
    customer = Customer.objects.get(pk=id_cust)

    address = Address.objects.get(pk=id_address, customer=customer)
    
    return {"customer_address": address}

@router.post("customers/{id_cust}/addresses.json", response=AddressRespon)
def  addAddress(request, id_cust:int, data:AddressIn):
    customer = Customer.objects.get(pk=id_cust)

    newAddress = Address.objects.create(customer=customer,
                           address1=data.address1,
                           address2=data.address2,
                           city=data.city,
                           province=data.province,
                           company=data.company,
                           phone=data.phone,
                           zip=data.zip,
                           default=data.default)
    
    return {"customer_address": newAddress}

@router.put("customers/{id_cust}/addresses/{id_address}.json", response=AddressRespon)
def updateAddress(request, id_cust:int, id_address:int, data:AddressIn):

    try:
        # Retrieve existing customer
        customer = Customer.objects.get(pk=id_cust)
        address = Address.objects.get(pk=id_address, customer=customer)

        address.address1 = data.address1
        address.address2 = data.address2
        address.city = data.city
        address.company = data.company
        address.phone = data.phone
        address.province = data.province
        address.country = data.country
        address.zip = data.zip
        address.save()
    
    except:
        return HttpResponse("Customer not found", status=404)
    
    return {"customer_address": address}

@router.put("customers/{id_cust}/addresses/{id_address}/default.json", response=AddressRespon)
def setDefaultAddress(request, id_cust:int, id_address:int):
    address = Address.objects.get(pk=id_address)
    address.default=True
    address.save()

    other = Address.objects.filter(customer_id=id_cust).exclude(id=id_address)
    for data in other:
        data.default=False
        data.save()
    
    return {"customer_address": [address]}

@router.delete("customers/{id_cust}/addresses/{id_address}.json")
def deleteAddress(request, id_cust:int, id_address:int):
    customer = Customer.objects.get(pk=id_cust)

    address = Address.objects.get(pk=id_address, customer=customer)
    address.delete()

    return {}