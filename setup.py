from setuptools import setup, find_packages

setup(
    name='flask-psx',
    version='0.0.1',
    packages=find_packages(),
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://example.com/flask-psx',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)