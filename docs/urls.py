'''This file is used to define the URL patterns for the API documentation. 
The SpectacularAPIView is used to generate the OpenAPI schema, which is then used by 
the SpectacularSwaggerView and SpectacularRedocView 
to generate the Swagger UI and ReDoc UI, respectively. 
The Swagger UI is a popular tool for visualizing and interacting with the API, 
while ReDoc is another tool that provides a more modern and responsive interface for 
API documentation. 
The URL patterns defined in this file will allow users to access the API documentation at 
the /api/schema/swagger-ui/ and /api/schema/redoc/ URLs.'''
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
