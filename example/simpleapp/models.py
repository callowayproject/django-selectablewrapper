from django.db import models

class Fruit(models.Model):
    """
    A simple model of fruit
    """
    
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name

class FavoriteFruit(models.Model):
    """A simple model to test foreign keys to fruits"""
    name = models.CharField(blank=True, max_length=100)
    fruit = models.ForeignKey(Fruit)
    
    def __unicode__(self):
        return "%s likes %s" % (self.name, self.fruit)

class FruitCombo(models.Model):
    """A simple model to test many-to-many keys to fruits"""
    name = models.CharField(blank=True, max_length=100)
    fruit = models.ManyToManyField(Fruit)
    
    def __unicode__(self):
        return "%s combo" % self.name
