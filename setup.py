from setuptools import setup, find_packages

requirements = ["beautifulsoup4==4.9.1", "requests==2.24.0"]

setup(
    name='statusinvest',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/thiagosalvatore/statusinvest-py',
    license='https://github.com/thiagosalvatore/statusinvest-py/blob/master/LICENSE',
    author='Thiago Salvatore',
    author_email='thiago.salvatore@gmail.com',
    description='Library to fetch information from status invest',
    install_requires=requirements,
)
