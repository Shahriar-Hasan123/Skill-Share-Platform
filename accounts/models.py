from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    location = models.CharField(max_length=150, blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return 'https://ui-avatars.com/api/?name=' + self.user.username + '&background=0D6EFD&color=fff&size=200'


class Skill(models.Model):

    CATEGORY_CHOICES = [
        ("technology", "Technology"),
        ("design", "Design"),
        ("business", "Business"),
        ("music", "Music"),
        ("language", "Language"),
        ("science", "Science"),
        ("sports", "Sports"),
        ("cooking", "Cooking"),
        ("art", "Art"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default="other"
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        unique_together = ["user", "name"]

    def __str__(self):
        return f"{self.name} ({self.user.username})"
