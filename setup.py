from setuptools import setup, find_packages

with open('requirements.txt', 'r') as fp:
    requirements = fp.read().splitlines()

setup(
    name='PingCog',
    version='1.0.1',
    license='MIT',
    description='Slash command example',
    author='@natsuki__yu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=requirements,
)
