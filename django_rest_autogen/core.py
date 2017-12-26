from rest_framework import viewsets, serializers, routers
from rest_framework.permissions import IsAdminUser
import rest_framework_filters as filters
from django.apps import apps
from rest_framework import filters



class AutoGenRouter(object):

    def _get_router(self, viewset_cls=None, serialiser_cls=None, permissions=None, include_filtering=False):
        autogen_router = routers.DefaultRouter()

        viewset_cls     = viewset_cls or viewsets.ModelViewSet
        serialiser_cls  = serialiser_cls or serializers.ModelSerializer
        permissions     = permissions or (IsAdminUser,)

        for mdl in apps.get_models():
            model = mdl
            resource_name = model.__name__

            cls_props = {
                'queryset': model.objects.all(),
                'permission_classes': permissions,
                'serializer_class': type('{0}Serialiser'.format(resource_name), (serialiser_cls,), {
                    'Meta': type('Meta', (object,), {
                        'model': model,
                        'fields': '__all__'
                    })
                })
            }

            if include_filtering:
                core_fields = [f for f in model._meta.get_fields() if not (
                    f.one_to_many or f.one_to_one or f.many_to_many
                )]

                cls_props['filter_class'] = type('{0}ModelFilter'.format(resource_name), (filters.FilterSet,), {
                    'Meta': type('Meta', (object,), {
                        'model': model,
                        'fields': core_fields
                    })
                })

            cls_config = type('{0}ViewSet'.format(resource_name), (viewset_cls,), cls_props)

            autogen_router.register(resource_name, cls_config)

        return autogen_router


    def get_default_router(self, include_filtering=True):
        '''
        Gets a default router pre-configured for all models
        :return: The default router pre-configured for all models
        '''
        return self._get_router(include_filtering)

