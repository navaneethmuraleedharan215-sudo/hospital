from django.urls import path
from complaints.views import Signupview,ComplaintListCreateView,ComplaintRetrieveUpdateDeleteView
from complaints.views import FilterByComplaintTypePriorityStatusView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[
    path('register/',Signupview.as_view()),
    path('token/',ObtainAuthToken.as_view()),
    path('hospital/',ComplaintListCreateView.as_view()),
    path('hospital/<int:pk>/',ComplaintRetrieveUpdateDeleteView.as_view()),
    path('hospital/filter/',FilterByComplaintTypePriorityStatusView.as_view()),
]