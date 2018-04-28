from django.conf.urls import url

from . import views,commit_view, onlogin_view

app_name = 'nppower'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^gdp$', views.GdpView.as_view(), name='gdp'),
    url(r'^race$', views.RaceView.as_view(), name='race'),
    url(r'^api/racelist$', commit_view.api_get_racelist, name='racejson'),
    url(r'^api/onlogin$', onlogin_view.create_session, name='csession'),
    url(r'^marathon/pacer$', views.PacerView.as_view(),name='pacer'),
    url(r'^marathon/post$', commit_view.post_race, name='post_race'),
    url(r'^marathon/delete$', commit_view.delete_race, name='delete_race'),
    
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
]
