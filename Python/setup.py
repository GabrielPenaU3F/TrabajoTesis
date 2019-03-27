import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name='MedidorAcustico',
    version='0.1',
    author="Gabriel Pena",
    author_email="gpena@untref.edu.ar",
    description="Medidor Acustico",
    long_description=long_description,
    url="https://github.com/GabrielPenaU3F/TrabajoTesis",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=[i.strip() for i in open("requirements.txt").readlines()]
)
