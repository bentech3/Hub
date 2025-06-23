from django.db import models

class HomepageContent(models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.TextField()

    def __str__(self):
        return self.heading

class AboutInfo(models.Model):
    vision = models.TextField()
    mission = models.TextField()
    values = models.TextField()

    def __str__(self):
        return "About Info"

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
