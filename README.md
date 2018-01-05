# django-rest-autogen
Autogenerate rest framework endpoints for your django models

## Basic Configuration
```
from django_rest_autogen.core import AutoGenRouter
router = AutoGenRouter().get_default_router()

urlpatterns += [
    url(r'^internal-api/', include(router.urls, namespace='internal_api')),
]
```

## Admin Models
You can restrict the auto-generation to only onclude models registered with your admin site
```
from django_rest_autogen.core import AutoGenRouter
router = AutoGenRouter().get_admin_site_router(include_filtering=True)

urlpatterns += [
    url(r'^internal-api/', include(router.urls, namespace='internal_api')),
]

```
Note: in this example we also enable filtering on all fields using:
```include_filtering=True``` 

## Open API Integration
django-rest-swagger provides convenient open-api compatible docs for all auto-generated endpoints
```
from rest_framework_swagger.views import get_swagger_view
urlpatterns += [
    url(r'^internal-api-swagger/', get_swagger_view(title='Internal API')),
]

```