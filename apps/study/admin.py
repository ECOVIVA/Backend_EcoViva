from django.contrib import admin
from .models import Category, Lesson, LessonCompletion

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')  
    search_fields = ('title',) 
    list_filter = ('categories',) 
    ordering = ('created_at',)
    filter_horizontal = ('categories',) 

@admin.register(LessonCompletion)
class LessonCompletionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'lesson', 'completed_at')
    search_fields = ('user__username', 'lesson__title')  
    list_filter = ('lesson',) 
    ordering = ('-completed_at',)

