from django.conf.urls import url
from main_app import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^([0-9]+)/$', views.dogprofile, name="dogprofile"),
    url(r'^new/$', views.post_dog, name="post_dog"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^delete/(?P<pk>\d+)$', views.delete_dog, name='delete_dog'),
    url(r'^edit/(?P<pk>\d+)$', views.update_dog, name='update_dog'),
    url(r'^signup/$', views.signup, name='signup'),
    # url(r'^post/$', views.post_dog, name="post_dog"),
    url(r'^about/$', views.about, name='about'),
    url(r'^filter/$', views.filter, name="filter"),
    url(r'^results/$', views.results, name="results")

]
