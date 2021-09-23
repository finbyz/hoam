from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in hoam/__init__.py
from hoam import __version__ as version

setup(
	name='hoam',
	version=version,
	description='Custom App',
	author='FinByz Tech Pvt Ltd',
	author_email='info@finbyz.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
