"""
URL configuration for patients in doctorapp project.

.views 
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))import Home
"""
# from django.urls import path
from rest_framework.routers import DefaultRouter

# from .views import (DepartmentDetailView, DepartmentListView,
#                     DoctorAvailabilityDetailView, DoctorAvailabilityView,
#                     MedicalNoteDetailView,
#                     MedicalNoteView)
from .viewsets import DoctorViewSet, DepartmentViewSet, DoctorAvailabilityViewSet, MedicalNoteViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('departments', DepartmentViewSet)
router.register('doctoravailabilities', DoctorAvailabilityViewSet)
router.register('medicalnotes', MedicalNoteViewSet)

urlpatterns = [
    # path('doctors/', DoctorListView.as_view()),
    # path('doctors/<int:pk>/', DoctorDetailView.as_view()),
    # path('departments/', DepartmentListView.as_view()),
    # path('departments/<int:pk>/', DepartmentDetailView.as_view()),
    # path('doctoravailabilities/', DoctorAvailabilityView.as_view()),
    # path('doctoravailabilities/<int:pk>/',
    #      DoctorAvailabilityDetailView.as_view()),
    # path('medicalnotes/', MedicalNoteView.as_view()),
    # path('medicalnotes/<int:pk>/', MedicalNoteDetailView.as_view()),
] + router.urls
