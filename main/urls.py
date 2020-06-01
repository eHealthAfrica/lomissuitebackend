from django.urls import path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from main.views import *

schema_view = get_swagger_view(title='LoMIS Suite API')

router = routers.DefaultRouter()
router.register('items', ItemViewSet)
router.register('locations', LocationViewSet)

urlpatterns = [
    path('doc/', schema_view)
]

urlpatterns += router.urls
