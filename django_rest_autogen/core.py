from rest_framework import viewsets, serializers, routers
from rest_framework.permissions import IsAdminUser
from django.apps import apps


class AutoGenRouter(object):

    def get_default_router(self):
        '''
        Gets a default router pre-configured for all models
        :return: The default router pre-configured for all models
        '''
        autogen_router = routers.DefaultRouter()

        for mdl in  apps.get_models():
            model = mdl
            resource_name = model.__name__

            ModelViewSet = type('{0}ViewSet'.format(resource_name), (viewsets.ModelViewSet,), {
                'queryset': model.objects.all(),
                'permission_classes': (IsAdminUser,),
                'serializer_class': type('{0}Serialiser'.format(resource_name), (serializers.ModelSerializer,), {
                    'Meta': type('Meta', (object,), {
                        'model': model,
                        'fields': '__all__'
                    })
                })
            })

            autogen_router.register(resource_name, ModelViewSet)

        return autogen_router

