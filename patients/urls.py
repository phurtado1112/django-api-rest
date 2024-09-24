"""
URL configuration for patients in doctorapp project.

.views 
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))import Home
"""
from django.urls import path

from patients.views import (
    PatientListView,
    PatientDetailView
)

urlpatterns = [
    path('patients/', PatientListView.as_view()),
    path('patients/<int:pk>/', PatientDetailView.as_view()),

]
