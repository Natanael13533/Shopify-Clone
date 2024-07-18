from ninja import Schema, Field
from typing import Optional, List
from pydantic import model_validator

from property.models import Country, Province

class ProvinceOut(Schema):
    id: int
    country_id: int
    name: str
    code: str
    tax_name: str
    tax_type: str
    tax: float
    tax_precentage: int

class ProvinceIn(Schema):
    country_id: Optional[int] = None
    name: str
    code: str
    tax_name: str
    tax_type: str
    tax: float

class ProvincesRespon(Schema):
    provinces: List[ProvinceOut]

class ProvinceRespon(Schema):
    province: ProvinceOut

class CountProvinces(Schema):
    count: int

class CountryIn(Schema):
    name: str
    code: str
    tax_name: str
    tax: float
    provinces: Optional[List[ProvinceIn]] = []

class CountryOut(Schema):
    id: int
    name: str
    code: str
    tax_name: str
    tax: float
    provinces: Optional[List[ProvinceOut]] = Field(alias='province_set')

class CountriesRespon(Schema):
    countries: List[CountryOut]

class CountryRespon(Schema):
    country: CountryOut

class CountCountries(Schema):
    count: int