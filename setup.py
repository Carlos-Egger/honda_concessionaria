from setuptools import setup, find_packages

setup(
    name="concessionaria-api",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'psycopg2-binary',
        'python-dotenv',
        'pytest',
    ],
)