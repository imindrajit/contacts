from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from contact_list.views import create_contact, contact_list, contact_detail, edit_contact, delete_contact, search

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'contacts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contactbook/', search, name = 'search-contact'),
    url(r'^create/', create_contact, name = 'create-contact'),
    url(r'^list/$', contact_list, name = 'contact-list'),
    url(r'^detail/(?P<contact_id>\d+)/$', contact_detail, name = 'contact-detail'),
    url(r'^edit/(?P<contact_id>\d+)/$', edit_contact, name="edit-contact"),
    url(r'^delete/(?P<contact_id>\d+)/$', delete_contact, name="delete-contact"),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += staticfiles_urlpatterns()
