from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^$', views.titleScreen),
		url(r'^worldmap/', views.worldmap),
		# A verfier pour cette url
		url(r'^battle/[0-9]+/', views.battle),
		url(r'^moviedex/', views.moviedex),
		#url Detail a rajouter
		url(r'^options/', views.options),
		url(r'^options/save_game', views.save),
		url(r'^options/load_game$', views.load),
		]

