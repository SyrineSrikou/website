from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
 path('admin/', admin.site.urls)
]
urlpatterns += i18n_patterns( 
    path('', include('pages.urls')),
    path('offers/', include('offers.urls')),
    path('contact/', include('contacts.urls')),
    path('references/', include('references.urls')),
    path('blog/', include('Blog.urls')),
    path('services/', include('services.urls')),
    prefix_default_language=False,   
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
