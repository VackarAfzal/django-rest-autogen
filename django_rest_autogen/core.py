from rest_framework import viewsets, serializers, routers
from rest_framework.permissions import IsAdminUser
from django.apps import apps


class AutoGenRouter(object):

    def _get_router(self, viewset_cls=None, serialiser_cls=None, permissions=None):
        autogen_router = routers.DefaultRouter()

        viewset_cls     = viewset_cls or viewsets.ModelViewSet
        serialiser_cls  = serialiser_cls or serializers.ModelSerializer
        permissions     = permissions or (IsAdminUser,)

        for mdl in apps.get_models():
            model = mdl
            resource_name = model.__name__

            cls_config = type('{0}ViewSet'.format(resource_name), (viewset_cls,), {
                'queryset': model.objects.all(),
                'permission_classes': permissions,
                'serializer_class': type('{0}Serialiser'.format(resource_name), (serialiser_cls,), {
                    'Meta': type('Meta', (object,), {
                        'model': model,
                        'fields': '__all__'
                    })
                })
            })

            autogen_router.register(resource_name, cls_config)

        return autogen_router


    def get_default_router(self):
        '''
        Gets a default router pre-configured for all models
        :return: The default router pre-configured for all models
        '''
        return self._get_router()

