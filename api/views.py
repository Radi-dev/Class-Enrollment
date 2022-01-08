from rest_framework import generics, permissions
from schema.permissions import IsUser
from schema.models import Applicant, Tutor, Course, Outline
from .serializers import ApplicantSerializer, TutorSerializer, CourseSerializer, OutlineSerializer


class ApplicantList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class ApplicantDetail(generics.RetrieveDestroyAPIView):
    #permission_classes = (IsUser or permissions.IsAdminUser, )
    permission_classes = (permissions.AllowAny, )
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class OutlineList(generics.ListCreateAPIView):
    queryset = Outline.objects.all()
    serializer_class = OutlineSerializer


class TutorList(generics.ListCreateAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
