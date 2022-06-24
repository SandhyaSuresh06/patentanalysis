from setuptools import find_packages, setup

setup(
    name='patentanalysis',
    packages=find_packages("src"),
    package_dir={"": "src"},
    version='0.1.0',
    description='Analyze and visualize the patent data',
    author='sandhyasuresh',
    license='',
)
