from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

# Create your models here.
from cms.models import CMSPlugin

class TimerData(CMSPlugin):
    """
     exploration of fieldsets
    """

    haha = models.CharField(
        verbose_name=_('Schrumdeidei'),
        max_length=255,
        help_text=_('stuff1'),
    )

    lala = models.CharField(
        verbose_name=_('zeuch'),
        max_length=255,
        help_text=_('stuff2'),
    )

    dudu = models.CharField(
        verbose_name=_('dingsda'),
        max_length=255,
        help_text=_('stuff3'),
    )
    

