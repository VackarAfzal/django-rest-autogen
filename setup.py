
from setuptools import setup


setup(
    name='django-rest-autogen',
    version='0.1.0',
    url='https://github.com/VackarAfzal/django-rest-autogen',
    author='Vackar Afzal',
    author_email='v.z.afzal@dundee.ac.uk',
    description=('A libarry to auto-gen rest-framework endpoint for all your django models.'),
    license='MIT',
    install_requires=['djangorestframework >= 3.6.3'],
    classifiers=[
        'Development Status :: Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Mit',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)