from django.db import models

# Create your models here.

IDEA_STATUS= (
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('done', 'done'),
    ('rejected', 'rejected')
)


OCENY= (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4')
)


WAGA= (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4')
)


PRZEDMIOTY= (
    ('przyroda', 'przyroda'),
    ('matma', 'matma'),
    ('fizyka', 'fizyka'),
    ('plastyka', 'plastyka')
)

class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(blank=True)
    status = models.CharField(choices=IDEA_STATUS, max_length=25, default='pending')
    def __str__(self):
        return self.title





class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()
    def __str__(self):
        return f'{self.id}'

''
class Ocenki(models.Model):
    school_objects = models.CharField(choices=PRZEDMIOTY, max_length=10)
    grade = models.CharField(choices=OCENY, max_length=30)
    weight = models.CharField(choices=WAGA, max_length=30)
    description = models.TextField(blank=True)