from django.db import models

class Topic(models.Model):
    text = models.CharField(max_length = 250)
    date_added = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField(blank = True, null = True)
    date_added = models.DateTimeField(auto_now_add = True) 
    date_updated = models.DateTimeField(auto_now = True)
    class Meta:
        verbose_name_plural = 'entries'   
    def __str__(self):
        return self.text
    