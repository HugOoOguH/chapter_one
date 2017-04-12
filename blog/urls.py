from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.PostList.as_view(), name='post_list'),
	url(r'^list/$', views.PostListView.as_view(), name='post_list_view'),
	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.PostDetail.as_view(), name="post_detail"),
]