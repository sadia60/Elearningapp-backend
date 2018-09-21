from django.db import models

# Create your models here.
class Course(models.Model):
    auther_name = models.CharField(max_length=50)
    course_title = models.CharField(max_length=50)
    course_description = models.CharField(max_length=100)
    course_created_timestamp=models.DateTimeField(auto_now_add=True)
    course_updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.auther_name} {0.course_title} {0.course_description}'
        return template.format(self)
        #return self.auther_name,self.course_title


class Video(models.Model):
    video_title = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()