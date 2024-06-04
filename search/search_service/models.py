from djongo import models

class Search(models.Model):
    key = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=20)

    def __str__(self):
        return self.key


