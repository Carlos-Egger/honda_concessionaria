from setuptools import setup, find_packages

setup(
    name="concessionaria-api",
    version="0.1",
    packages=find_packages(where='.'),
    package_dir={'': '.'},
    install_requires=[
        'flask>=2.0.1',
        'flask-sqlalchemy>=2.5.1',
        'psycopg2-binary>=2.9.1',
        'python-dotenv>=0.19.0',
        'pytest>=7.0.1',
        'pytest-cov>=3.0.0',
        'flake8>=4.0.1'
    ],
    python_requires='>=3.9',
)