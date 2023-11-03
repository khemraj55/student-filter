from django.db import models
from django.core.exceptions import ValidationError

def upload_path_handler(instance, filename):
    return "images/{}".format(filename)


def unique_roll_no_validator(value, class_name):
    students = Student.objects.filter(roll_no=value, class_name=class_name)
    if students.exists():
        raise ValidationError('A student with this roll number already exists in the same class.')


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    subject1 = models.CharField(max_length=100)
    subject2 = models.CharField(max_length=100)
    subject3 = models.CharField(max_length=100)
    subject4 = models.CharField(max_length=100)
    subject5 = models.CharField(max_length=100)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    score3 = models.IntegerField()
    score4 = models.IntegerField()
    score5 = models.IntegerField()
    image = models.ImageField(upload_to=upload_path_handler, blank=True, null=True,)
    class_name = models.IntegerField(choices=[(i, i) for i in range(1, 13)])
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(Student, self).save(*args, **kwargs)

    def clean(self):
        unique_roll_no_validator(self.roll_no, self.class_name)

    def __str__(self):
        return self.name