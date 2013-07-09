from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse


class Player(models.Model):
    user = models.ForeignKey(get_user_model(), blank=True, null=True)

    # Fields if this isn't tied to a user
    _first_name = models.CharField(max_length=255, blank=True, null=True)
    _last_name = models.CharField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('player_detail', args=(), kwargs={'pk': self.pk})

    def get_from_self_or_user(self, field_name):
        if self.user:
            return getattr(self.user, field_name)
        else:
            return getattr(self, '_%s' % field_name)

    @property
    def first_name(self):
        return self.get_from_self_or_user('first_name')

    @property
    def last_name(self):
        return self.get_from_self_or_user('last_name')
