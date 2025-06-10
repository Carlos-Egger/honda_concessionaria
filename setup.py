from setuptools import setup, find_packages

setup(
    name="concessionaria-api",
    version="0.1",
    packages=find_packages(include=['app*']),
    package_dir={'': '.'},
    package_data={
        'app': ['routes/*.py', 'services/*.py', 'models/*.py']
    },
    install_requires=[...]
)