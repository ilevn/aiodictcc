from distutils.core import setup

setup(
    name='aiodictcc',
    version='1.0.0',
    packages=['aiodictcc'],
    url='https://github.com/ilevn/aiodictcc',
    license='MIT',
    author='Nils Theres',
    author_email='nilsntth@gmail.com',
    description='An asyncio wrapper for dict.cc',
    install_requires=[
        "aiohttp==1.3.3",
        "async-timeout==1.1.0",
        "chardet==2.3.0",
        "lxml==3.7.3",
        "multidict==2.1.4",
        "wheel==0.24.0",
        "yarl==0.9.8"
    ]
)
