from ninja import Schema, ModelSchema, FilterSchema, Field
from datetime import datetime
from typing import Optional, List, Self
from pydantic import model_validator

from customer.models import Customer, Address

class AddressIn(Schema):
    customer_id: Optional[int] = None
    address1: str
    address2: Optional[str] = None
    city: str
    company: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    province: str
    country: str
    zip: str
    name: Optional[str] = ''
    default: Optional[bool] = False

class AddressOut(Schema):
    id: int
    customer_id: int
    first_name: str = Field(alias='customer.user.first_name')
    last_name: str = Field(alias='customer.user.last_name')
    company: str
    address1: str
    address2: str
    city: str
    province: str
    country: str
    zip: str
    phone: Optional[str] = ''
    name: str
    default: bool

class AddressRespon(Schema):
    customer_address: AddressOut

class AddressesRespon(Schema):
    addresses: List[AddressOut]

class CustomerOut(Schema):
    id: int
    email: str = Field(alias='user.email')
    created_at: datetime
    updated_at: datetime
    first_name: str = Field(alias='user.first_name')
    last_name: str = Field(alias='user.last_name')
    order_counts: int
    state: str
    verified_email: bool
    currency: str
    phone: str
    addresses: Optional[List[AddressOut]] = Field(alias='address_set')

class CustomerIn(Schema):
    email: str
    first_name: str
    last_name: str
    state: str
    verified_email: bool
    send_email_welcome: bool
    currency: str
    phone: str
    addresses: Optional[List[AddressIn]] = []

class CustomerInUpdate(Schema):
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    state: Optional[str]
    verified_email: Optional[bool]
    send_email_welcome: Optional[bool]
    currency: Optional[str]
    phone: Optional[str]
    addresses: Optional[List[AddressOut]] = None

def parse_query(query_str: str):
    filters = {}
    for param in query_str.split(','):
        key, value = param.split(':')
        filters[key] = value
    return filters

class CustomerRespon(Schema):
    customers: List[CustomerOut]

class SingleCustomerRespon(Schema):
    customer: CustomerOut

class CountCustomer(Schema):
    count: int