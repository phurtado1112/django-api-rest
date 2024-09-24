"""
URL configuration for patients in doctorapp project.

.views 
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))import Home
"""
# from django.urls import path

# from .views import (
#     AppointmentListView,
#     AppointmentDetailView,
#     MedicalNoteListView,
#     MedicalNoteDetailView
# )

from rest_framework.routers import DefaultRouter

from .viewsets import AppointmentViewSet, MedicalNoteViewSet

router = DefaultRouter()

router.register('appointments', AppointmentViewSet)
router.register('medicalnotes', MedicalNoteViewSet)

urlpatterns = [
    # path('bookings/', AppointmentListView.as_view()),
    # path('bookings/<int:pk>/', AppointmentDetailView.as_view()),
    # path('medical-notes/', MedicalNoteListView.as_view()),
    # path('medical-notes/<int:pk>/', MedicalNoteDetailView.as_view()),
] + router.urls
