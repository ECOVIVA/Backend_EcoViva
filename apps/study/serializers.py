from rest_framework import serializers
from .models import Lesson, LessonCompletion

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonCompletion
        fields = ['user', 'lesson', 'completed_at']
        read_only_fields = ['completed_at']
    
    def create(self, validated_data):
        user = validated_data['user']
        lesson = validated_data['lesson']

        if LessonCompletion.objects.filter(user=user, lesson=lesson).exists():
            raise serializers.ValidationError("O Usuario já concluiu essa lição.")

        return super().create(validated_data)
