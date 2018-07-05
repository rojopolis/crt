import versioneer
from setuptools import find_packages, setup
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
)
