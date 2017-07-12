from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add/$', views.add, name='add'),
	url(r'^addEvent/$', views.addEvent, name='addEvent'),
	url(r'^editForm/$', views.editForm, name='editForm'),
	url(r'^render/$', views.renderForm, name='renderForm'),
	url(r'^login/$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^response/$', views.responseForm, name='responseForm'),
]