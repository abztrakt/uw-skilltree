from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LearningConcept(models.Model):
    """ Represents metadata about a concept that need
        to be learned.
    """
    title = models.CharField(max_length=60)
    url = models.URLField()
    description = models.TextField()
    prerequisite = models.ManyToManyField('self', through='Prerequisite', symmetrical=False)
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return self.title

class Prerequisite(models.Model):
    """
    """
    # the base skill
    from_concept = models.ForeignKey('LearningConcept', related_name='from_concept')
    # its children skills
    to_concept = models.ManyToManyField('LearningConcept', related_name='to_concept')

    def __unicode__(self):
        return self.from_concept.title

class Category(models.Model):
    """ Repesents a larger categorization of the learning concepts.
    """
    title = models.CharField(max_length=60)

    def __unicode__(self):
        return self.title

class Completed(models.Model):
    date_completed = models.DateField()
    date_verified = models.DateField()
    user = models.OneToOneField(User)
    concept = models.OneToOneField('LearningConcept')
