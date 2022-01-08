from rest_framework import serializers
from schema.models import Applicant, Tutor, Course, Outline


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class OutlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outline
        fields = '__all__'
