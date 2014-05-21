from setuptools import setup, find_packages

setup(
        name = 'bmer',
        author = 'JChien',
        author_email = 'jeffchien13@gmail.com',
        description = 'manage executable files',
        version = '0.0.2',
        license = 'MIT License',
        packages = find_packages(),
        entry_points = {
            'console_scripts': ['bmer = bmer.main:main']
        },
        install_requires = [
            'docopt>=0.6'
        ],
)
