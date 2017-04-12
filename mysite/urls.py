from django.conf.urls import url, include
from django.contrib import admin
from blog import urls as blogUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include(blogUrls, namespace="blog")),
]
