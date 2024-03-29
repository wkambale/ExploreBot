from django.urls import include,path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'destinations',views.DestinationViewSet)
router.register(r'hotels',views.HotelsViewSet)
router.register(r'trips',views.TripsViewSet)
router.register(r'tourguides',views.TourViewSet)
router.register(r'facts',views.FactsViewSet)
router.register(r'tweets',views.TweetsViewSet)
router.register(r'animals',views.AnimalViewSet)
router.register(r'tourcompanies',views.TourCompaniesViewSet)
router.register(r'updates',views.updatesViewSet)
router.register(r'carhire',views.CarHireViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]