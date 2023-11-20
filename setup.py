from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Front-Clientes',
    version='1.0',
    description='Front End para la api de clientes',
    author='Raul Andres Orlando',
    author_email='orlando.raul.andres@outlook.com',
    url='https://github.com/rolito223/front-clientes',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=requirements,
)
