from django.urls import path, include
from .views import CourseViewSet, ApplicantViewSet, TutorViewSet, OutlineViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('courses', CourseViewSet)
router.register('students', ApplicantViewSet)
router.register('tutors', TutorViewSet)
router.register('outlines', OutlineViewSet)

urlpatterns = [
    path('', include(router.urls)),

]


# urlpatterns = [
#    path('courses/', CourseList.as_view(), name='courses'),
#    path('courses/<int:pk>/', CourseDetail.as_view(), name='course'),
#    path('students/', ApplicantList.as_view(), name='students'),
#    path('students/<int:pk>/', ApplicantDetail.as_view(), name='student'),
#    path('tutors/', TutorList.as_view(), name='tutors'),
#    path('outlines/', OutlineList.as_view(), name='outlines'),
#    #path('ref/', RefList.as_view(), name='ref')
#
# ]
