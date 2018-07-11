from os import path
import versioneer
from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

INSTALL_REQUIRES = ([i.strip() for i in open("requirements.txt").readlines()])
setup(
    name='crt',
    author='Robert Jordan',
    author_email='rojopolis@deba.cl',
    url='https://github.com/rojopolis/crt/wiki',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    entry_points='''
        [console_scripts]
        crt=crt.cli:cli
    ''',
    download_url='https://github.com/rojopolis/crt/releases/latest',
    description='Cloud Render Toolkit',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
