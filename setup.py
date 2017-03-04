from setuptools import setup

setup(
    name='aiodictcc',
    version='1.0.7',
    packages=['aiodictcc'],
    url='https://github.com/ilevn/aiodictcc',
    license='MIT',
    author='Nils Theres',
    author_email='nilsntth@gmail.com',
    description='An asyncio wrapper for dict.cc',
    install_requires=[
        "aiohttp>=1.0.0,<=1.3.3",
        "lxml==3.7.3",
    ]
)
