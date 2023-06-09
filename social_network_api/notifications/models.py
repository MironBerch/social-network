from django.db import models

from accounts.models import User
from posts.models import Post


class Notification(models.Model):

    class NotificationTypes(models.IntegerChoices):
        REPOST = 1
        LIKE_POST = 2
        REPLY = 3
        FOLLOW = 4

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notification_from_user',
    )
    is_read = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='notification_post',
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications',
    )
    type = models.PositiveIntegerField(
        choices=NotificationTypes.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'

    def __str__(self):
        return f'{self.from_user} => {self.to_user}: {self.type}'
