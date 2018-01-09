
from setuptools import setup


setup(
    name='django-rest-autogen',
    version='0.2.9',
    url='https://github.com/VackarAfzal/django-rest-autogen',
    author='Vackar Afzal',
    author_email='v.z.afzal@dundee.ac.uk',
    description=('A libarry to auto-gen rest-framework endpoint for all your django models.'),
    license='MIT',
    packages=['django-rest-autogen'],
    install_requires=['djangorestframework >= 3.6.3', 'djangorestframework-filters==0.10.2'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
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
