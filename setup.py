from setuptools import find_packages, setup

setup(
    name='query_to_csv',
    packages=find_packages('src'),
    version='0.0.1',
    description='write data of query to csv',
    author='Niklas R.',
    package_dir={"": "src"},
)
