from django.db import models


class Hackathon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(
        upload_to='hackathon_images/background_images')
    hackathon_image = models.ImageField(
        upload_to='hackathon_images/hackathon_images')
    TYPE_CHOICES = (
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    )
    submission_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=10, decimal_places=2)

    participants = models.ManyToManyField(
        'user.User', related_name='registered_hackathons')
