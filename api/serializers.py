from rest_framework import serializers
from schema.models import Applicant, Tutor, Course, Outline


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class OutlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outline
        fields = ('course', 'title', 'description')


class CourseSerializer(serializers.ModelSerializer):
    tutor = TutorSerializer(read_only=True)
    outline = OutlineSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Course
        fields = ('title', 'description', 'tutor', 'outline')


class ApplicantSerializer(serializers.ModelSerializer):
    #course = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Applicant
        fields = '__all__'
