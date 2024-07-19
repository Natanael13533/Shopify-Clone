from ninja import NinjaAPI

from ninja_simple_jwt.auth.views.api import mobile_auth_router
from ninja_simple_jwt.auth.ninja_auth import HttpJwtAuth

from customer.api import router as customers_router
from property.api import router as properties_router

api = NinjaAPI()
api.add_router("/auth/", mobile_auth_router)
apiAuth = HttpJwtAuth()

api.add_router("", customers_router, auth=apiAuth)
api.add_router("", properties_router, auth=apiAuth)