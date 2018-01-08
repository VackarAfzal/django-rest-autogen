# django-rest-autogen
Autogenerate rest framework endpoints for your django models

## Basic Configuration
```python
from django_rest_autogen.core import RouterFactory
router = RouterFactory().get_default_router()

urlpatterns += [
    url(r'^internal-api/', include(router.urls, namespace='internal_api')),
]
```

## Admin Models
You can restrict the auto-generation to only onclude models registered with your admin site
```python
from django_rest_autogen.core import RouterFactory
router = RouterFactory().get_admin_site_router(include_filtering=True)

urlpatterns += [
    url(r'^internal-api/', include(router.urls, namespace='internal_api')),
]

```
Note: in this example we also enable filtering on all fields using:
```include_filtering=True``` 

## Open API Integration
django-rest-swagger provides convenient open-api compatible docs for all auto-generated endpoints
```python
from rest_framework_swagger.views import get_swagger_view
urlpatterns += [
    url(r'^internal-api-swagger/', get_swagger_view(title='Internal API')),
]

```

## Shorthand
Shorthand method for getting up an running
```python
from django_rest_autogen.registration import register_router


router = RouterFactory().get_admin_site_router(include_filtering=True)
register_router(
    router,
    urlpatterns,
    api_url='admin-api',
    version=1,
    namespace='internal_admin_site',
    open_api_suffix='open-api',
    open_api_title='Admin API'
)

```
Then simply go to these urls to see you auto generated admin apis

http://mysite.com/admin-api/

http://mysite.com/admin-api/open-api