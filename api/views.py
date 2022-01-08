from rest_framework import generics, permissions, viewsets
from schema.permissions import ListOrRetrieveIfNotAdmin, NoListIfNotStaff
from schema.models import Applicant, Tutor, Course, Outline
from .serializers import ApplicantSerializer, TutorSerializer, CourseSerializer, OutlineSerializer


class ApplicantViewSet(viewsets.ModelViewSet):
    permission_classes = (NoListIfNotStaff, )
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class CourseViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsUser or permissions.IsAdminUser, )
    permission_classes = (ListOrRetrieveIfNotAdmin,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class OutlineViewSet(viewsets.ModelViewSet):
    permission_classes = (ListOrRetrieveIfNotAdmin,)
    queryset = Outline.objects.all()
    serializer_class = OutlineSerializer


class TutorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
