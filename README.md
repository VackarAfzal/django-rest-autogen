# django-rest-autogen
Autogenerate rest framework endpoints for all your django models

##Basic Configuration
```
from django_rest_autogen.core import AutoGenRouter
router = AutoGenRouter().get_default_router()

urlpatterns += [
    url(r'^internal-api/', include(router.urls, namespace='internal_api')),
]
```

##Open API Integration
django-rest-swagger provides convenient open-api compatible docs for all auto-generated endpoints
```
from rest_framework_swagger.views import get_swagger_view
urlpatterns += [
    url(r'^internal-api-swagger/', get_swagger_view(title='Internal API')),
]

```