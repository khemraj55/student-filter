from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    total_score = serializers.SerializerMethodField()

    def get_total_score(self, obj):
        return obj.score1 + obj.score2 + obj.score3 + obj.score4 + obj.score5

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_no', 'subject1', 'subject2', 'subject3', 'subject4', 'subject5',
                  'score1', 'score2', 'score3', 'score4', 'score5', 'image', 'class_name', 'total_score']
