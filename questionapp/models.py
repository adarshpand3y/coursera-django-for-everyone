from django.db import models

# Create your models here.
class Question(models.Model):
    questiontext = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.questiontext

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.SmallIntegerField()