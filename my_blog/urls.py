from django.conf.urls import include, url
from django.contrib import admin
from article import urls as article_urls
urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include(article_urls))
]
