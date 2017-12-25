from django.conf.urls import url
from . import views

urlpatterns = [
	#poster_app --> homepage
    url(r'^$',views.index, name = 'index'),
    #poster_app/opportunities
    url(r'^(?P<poster_opportunities>[0-9]+)/$',views.opportunities, name = 'opportunities')
]