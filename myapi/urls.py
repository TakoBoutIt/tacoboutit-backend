from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)
# router.register(r'restaurants', views.RestaurantViewSet, basename='restaurant')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # The line below allows us to retrieve restaurants from the db but not post
    # path('api/', include(router.urls)),
    # The line below will allow us to post restaurants but not return them to the user
    # also note that def get() but not be nested under RestaurantViewSet, but on the same level
    path('api/restaurants/', views.RestaurantViewSet.retrieve, name='list'),
    # path('restaurants', views.RestaurantViewSet, name='movies'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]