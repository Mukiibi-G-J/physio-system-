from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
]
handler404 = "main.views.page_not_found"


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
