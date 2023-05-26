from django.db import models

# Create your models here.
class Artiles(models.Model):
    title = models.CharField('Name', max_length=50)
    announcement = models.CharField('Announcement', max_length=250)
    full_text = models.TextField('Text')
    date = models.DateTimeField('Date')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}' 
    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'