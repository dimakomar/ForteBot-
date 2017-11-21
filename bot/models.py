from django.db import models

# Create your models here.
class Message(models.Model):
    author_id = models.ForeignKey('auth.User')
    text = models.TextField()

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title