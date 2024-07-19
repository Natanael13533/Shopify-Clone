from ninja import Router
from django.http import HttpResponse

from property.models import Country, Province
from property.schemas import ProvincesRespon, ProvinceRespon, CountProvinces, ProvinceIn, CountryIn, CountryRespon, CountriesRespon, CountCountries

router = Router()

# PROVINCE
@router.get("countries/{id_coun}/provinces.json", response=ProvincesRespon)
def getAllProvinces(request, id_coun:int):
    country = Country.objects.get(pk=id_coun)

    provinces = Province.objects.filter(country=country)
    
    return {"provinces": provinces}

@router.get("countries/{id_coun}/provinces/{id_prov}.json", response=ProvinceRespon)
def getSingleProvince(request, id_coun:int, id_prov:int):
    country = Country.objects.get(pk=id_coun)

    province = Province.objects.get(pk=id_prov, country=country)
    
    return {"province": province}

@router.get("countries/{id_coun}/provinces/count/count.json", response=CountProvinces)
def count_provinces(request, id_coun:int):
    country = Country.objects.get(pk=id_coun)

    countProv = Province.objects.filter(country=country).count()
    
    return {"count": countProv}

@router.put("countries/{id_coun}/provinces/{id_prov}.json", response=ProvinceRespon)
def updateProvince(request, id_coun:int, id_prov:int, data:ProvinceIn):

    try:
        # Retrieve existing customer
        country = Country.objects.get(pk=id_coun)
        province = Province.objects.get(pk=id_prov, country=country)

        province.name = data.name
        province.code = data.code
        province.tax_name = data.tax_name
        province.tax_type = data.tax_type
        province.tax = data.tax
        province.save()
    
    except:
        return HttpResponse("Province not found", status=404)
    
    return {"province": province}

@router.post("countries.json", response=CountryRespon)
def addCountry(request, data:CountryIn):
    newCountry = Country.objects.create(code=data.code,
                                        name=data.name,
                                        tax_name=data.tax_name,
                                        tax=data.tax)
    
    if data.provinces:
        for province_data in data.provinces:
            province = Province.objects.create(country=newCountry,
                                               code=province_data.code,
                                               name=province_data.name,
                                               tax_name=province_data.tax_name,
                                               tax_type=province_data.tax_type,
                                               tax=province_data.tax)
            
            newCountry.province_set.add(province)
    
    return {"country" : newCountry}

@router.get("countries.json", response=CountriesRespon)
def getAllCountries(request):
    countries = Country.objects.all().prefetch_related('province_set')

    return {"countries" : countries}

@router.get("countries/{id_coun}.json", response=CountryRespon)
def getSingleCountries(request, id_coun:int):
    country = Country.objects.get(pk=id_coun)

    return {"country" : country}

@router.get("countries/count/count.json", response=CountCountries)
def count_countries(request):
    country = Country.objects.count()
    
    return {"count": country}

@router.put("countries/{id_coun}.json", response=CountryRespon)
def updateCountry(request, id_coun:int, data:CountryIn):

    try:
        # Retrieve existing customer
        country = Country.objects.get(pk=id_coun)

        country.name = data.name
        country.code = data.code
        country.tax_name = data.tax_name
        country.tax = data.tax
        country.save()
    
    except:
        return HttpResponse("country not found", status=404)
    
    return {"country": country}

@router.delete("countries/{id_coun}.json")
def deleteCountry(request, id_coun:int):
    country = Country.objects.get(pk=id_coun)

    country.delete()

    return {}