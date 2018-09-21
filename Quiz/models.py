from django.db import models
from Dashboard.models import Video

# Create your models here.
# one video has one quiz
class Mcq(models.Model):
    video= models.ForeignKey(Video, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=250)
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)
    choice3 = models.CharField(max_length=100)
    choice4 = models.CharField(max_length=100)
    correct_choice = models.CharField(max_length=100)
    question_created_timestamp=models.DateTimeField(auto_now_add=True)
    question_updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.question_text} {0.choice1} {0.choice2}{0.choice3}{0.choice4}{0.{0.correct_choice}}'
        return template.format(self)
        #return self.auther_name,self.course_title


# 1 Quiz have 1 result so we have quiz or question id in
class Result(models.Model):
    quizquestion = models.ForeignKey(Mcq, on_delete=models.CASCADE)
    quiz_taken=models.BooleanField(default=False)
    quiz_marks = models.IntegerField(default=0)

    #video_next_url=models.CharField(max_length=1000)
    def __str__(self):
        template = '{0.quizquestion} {0.quiz_taken} {0.video_watched}{0.video_next_url}'
        return template.format(self)

