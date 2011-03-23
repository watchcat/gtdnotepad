from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, unique=True)
    #TODO: projects can be nested
    def __unicode__(self):
        return 'User: %s, Project: %s'%(self.user, self.name)

class Note(models.Model):
    name = models.CharField("Note header",max_length=255)
    status = models.IntegerField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name

class NoteItem(models.Model):
    data = models.TextField()
    note =models.ForeignKey(Note)
    
    def __unicode__(self):
        return self.data

