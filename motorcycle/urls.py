from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path('', include('motorcycle.core.urls')),
    path('motorcycle/', include('motorcycle.motor.urls')),
    path('included/', include('motorcycle.included_in_the_price.urls')),
    path('rent/', include('motorcycle.rent.urls')),
    path('accessory/', include('motorcycle.accessory.urls')),
    path('tour/', include('motorcycle.tour.urls')),
    path('about-us/', include('motorcycle.about_us.urls')),
    path('blog/', include('motorcycle.blog.urls')),
    path('faq/', include('motorcycle.faq.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('motorcycle.core.urls')),
    path('motorcycle/', include('motorcycle.motor.urls')),
    path('included/', include('motorcycle.included_in_the_price.urls')),
    path('rent/', include('motorcycle.rent.urls')),
    path('accessory/', include('motorcycle.accessory.urls')),
    path('tour/', include('motorcycle.tour.urls')),
    path('about-us/', include('motorcycle.about_us.urls')),
    path('blog/', include('motorcycle.blog.urls')),
    path('faq/', include('motorcycle.faq.urls')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

# Allow us to use media file
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )