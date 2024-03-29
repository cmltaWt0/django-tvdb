import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name='django-tvdb',
        version='0.1',
        packages=['tvdb'],
        include_package_data=True,
        license='The MIT License: http://www.opensource.org/licenses/mit-license.php',
        description='A simple Django app for TV channels DB.',
        long_description=README,
        author='Maksym Sokolsky',
        author_email='misokolsky@gmail.com',
        classifiers=[
                    'Environment :: Web Environment',
                    'Framework :: Django',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: OS Independent',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Python :: 2.7',
                    'Topic :: Internet :: WWW/HTTP',
                    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                ],
)
