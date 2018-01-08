import logging

from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

logger = logging.getLogger()


def register_router(
        router,
        urlpatterns,
        api_url='site-api',
        version=1,
        namespace='site_api',
        open_api_suffix='open-api',
        open_api_title='Site API'
):
    logger.info('Registering router under namespace: {0}'.format(namespace))
    urlpatterns += [
        url(r'^{0}/v{1}/?'.format(api_url, version), include(router.urls, namespace=namespace)),
        url(r'^{0}/v{1}/{2}/?'.format(api_url, version, open_api_suffix), get_swagger_view(title=open_api_title)),
    ]

    return urlpatterns
