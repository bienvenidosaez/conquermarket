from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from rest_framework import routers

from marketplace.products.api.product_api import (
    ProductViewSet,
    MyProductsViewSet,
    CreateProductView,
    Reset
)
from marketplace.buyers.api.buyer_api import BuyerViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'buyers', BuyerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('myproducts/<str:buyer_uuid>/', MyProductsViewSet.as_view()),
    path('createproduct/', CreateProductView.as_view()),
    path('reset/', Reset.as_view()),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if 'debug_toolbar' in settings.INSTALLED_APPS and settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]

admin.site.index_title = "Conquer Market Place"
admin.site.site_header = "Conquer Market Place"
admin.site.site_title = "Conquer Market Place"
