from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, null=True),
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/'),


class About(models.Model):
    title = models.CharField(max_length=255, null=True),
    desc = models.TextField(),
    image = models.ImageField(upload_to='about/images/'),


class Investment(models.Model):
    title = models.CharField(max_length=255, null=True),
    desc = models.TextField(),
    image = models.ImageField(upload_to='investments/images/'),


class Project(models.Model):
    title = models.CharField(max_length=255, null=True),
    desc = models.TextField(),
    image = models.ImageField(upload_to='projects/images/'),