from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user', views.UserView)
router.register('register', views.RegisterView)
router.register('person', views.PersonView)
router.register('branch', views.BranchView)
router.register('country', views.CountryView)
router.register('state', views.StateView)
# router.register('user', views.UserView)

urlpatterns = [
    path('', include(router.urls))
]
