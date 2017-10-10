from django.db import models

__all__ = (
    'InstagramUser',
)

class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    # symmetrical=False
    # 자기 자신을 참조하는 following 1개 필드 생성
    following = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
    )

