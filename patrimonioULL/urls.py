from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings as st
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'patrimonioULL.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^patrimonioarte/admin/', include(admin.site.urls)),
    url(r'^patrimonioarte/tinymce/', include('tinymce.urls')),
    url(r'^patrimonioarte/accounts/login/$',
        'django_cas.views.login',
        name='login'),
    url(r'^patrimonioarte/accounts/logout/$',
        'django_cas.views.logout',
        name='logout'),
)

if st.DEBUG:
    urlpatterns += static(st.MEDIA_URL, document_root=st.MEDIA_ROOT)
