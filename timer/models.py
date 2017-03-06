from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

# Create your models here.
from cms.models import CMSPlugin

class TimerData(CMSPlugin):
    """
     exploration of fieldsets
    """

    rest_url = models.CharField(
        verbose_name=_('GET url'),
        max_length=255,
        help_text=_('url für REST api'),
        default = "/api/clock/now?format=json"
    )

    background = models.CharField(
        verbose_name=_('background color'),
        max_length=255,
        default = 'white',
        help_text=_('background color name')
    )

    interval = models.IntegerField(
        verbose_name=_('Interval'),
        help_text=_('interval in s'),
        default = 60
    )
    

