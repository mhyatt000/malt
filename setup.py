from setuptools import setup, find_packages

setup(
    name='malt',
    version='0.1',
    packages=find_packages(),
    description='MAchine Learning Toolbox',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Matt Hyatt',
    author_email='mhyatt000@gmail.com',
    url='https://github.com/mhyatt000/malt/',
    install_requires=[
        # List your project dependencies here
        # For example:
        # 'numpy>=1.15.4',
        # 'pandas>=0.23.4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.11.2',
    ],
)
