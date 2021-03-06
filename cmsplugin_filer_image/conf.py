#-*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from appconf import AppConf


class CmspluginFilerImageAppConf(AppConf):
    STYLE_CHOICES = (
        # ('default', _('Default')),  # define your styles here.
    )
    DEFAULT_STYLE = ''

    def configure(self):
        # set DEFAULT_STYLE to '' if it is not in STYLE_CHOICES
        if not self.configured_data['DEFAULT_STYLE'] in [s for s, l in self.configured_data['STYLE_CHOICES']]:
            self.configured_data['DEFAULT_STYLE'] = ''
        return self.configured_data
