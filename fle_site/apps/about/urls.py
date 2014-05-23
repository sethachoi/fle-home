from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('fle_site.apps.about.views',
    url(r'^$', TemplateView.as_view(template_name='about/mission.html'), name='mission'),
    url(r'^team/$', 'team', name='team'),
    url(r'^board/$', 'board', name='board'),
    url(r'^supporters/$', 'supporters', name='supporters'),
    url(r'^press/$', 'press', name='press'),
    url(r'^internships/$', 'internships', name='internships'),
)