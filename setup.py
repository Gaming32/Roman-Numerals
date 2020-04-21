import setuptools

setuptools.setup(
    name = 'Roman Numerals Simple',
    version = '1.0.1',
    url = 'https://github.com/gaming32/roman-numerals',
    author = 'Gaming32',
    author_email = 'gaming32i64@gmail.com',
    license = 'License :: OSI Approved :: MIT License',
    description = 'Library for interacting with roman numerals',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    install_requires = [

    ],
    py_modules = [
        'roman',
    ],
)