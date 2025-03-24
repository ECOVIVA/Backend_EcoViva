from django.db import models
from django.core.exceptions import ValidationError
from apps.users.models import Users

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    """Representa uma categoria de lição."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessions"

    """Representa uma lição disponível para os usuários concluírem."""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class LessonCompletion(models.Model):
    class Meta:
        verbose_name = "LessonCompletion"
        verbose_name_plural = "LessionsCompletion"
        unique_together = ('user', 'lesson')  

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """Valida se a lição já foi concluída pelo usuário antes de salvar."""
        if LessonCompletion.objects.filter(user=self.user, lesson=self.lesson).exists():
            raise ValidationError("Você já completou essa lição.")

    def save(self, *args, **kwargs):
        """Executa a validação antes de salvar."""
        self.full_clean()  # Chama `clean()` automaticamente antes de salvar
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} completed {self.lesson.title}"

