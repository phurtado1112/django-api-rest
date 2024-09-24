"""
URL configuration for patients in doctorapp project.

.views 
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))import Home
"""
# from django.urls import path
# from patients.views import (
#     PatientListView,
#     PatientDetailView
# )
from rest_framework.routers import DefaultRouter

from .viewsets import PatientViewSet, MedicalRecordViewSet, InsuranceViewSet

router = DefaultRouter()

router.register('patients', PatientViewSet)
router.register('medicalrecords', MedicalRecordViewSet)
router.register('insurances', InsuranceViewSet)


urlpatterns = [
    # path('patients/', PatientListView.as_view()),
    # path('patients/<int:pk>/', PatientDetailView.as_view()),
] + router.urls
