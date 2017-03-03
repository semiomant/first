from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from datetime import datetime

class TimerPlugin(CMSPluginBase):
    model = CMSPlugin
    name  = "timer" 
    render_template = "timer/timer.html"
    cache = False

    def render(self, context, instance, placeholder):
        #now = datetime.now()
        context.update({'now': datetime.now()})
        return context

plugin_pool.register_plugin(TimerPlugin)