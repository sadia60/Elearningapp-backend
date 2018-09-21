from django.db import models

# Create your models here.
class Course(models.Model):
    auther_name = models.CharField(max_length=50)
    course_title = models.CharField(max_length=100)
    course_description = models.CharField(max_length=1000)
    course_created_timestamp=models.DateTimeField(auto_now_add=True)
    course_updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.auther_name} {0.course_title} {0.course_description}'
        return template.format(self)
        #return self.auther_name,self.course_title

# 1 course have amny videos so fk of course in many
class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video_url = models.CharField(max_length=1000)
    video_watched = models.BooleanField(default=False)
    video_next_url=models.CharField(max_length=1000)
    #video_next_url=models.CharField(max_length=1000)
    def __str__(self):
        template = '{0.course} {0.video_url} {0.video_watched}{0.video_next_url}'
        return template.format(self)
