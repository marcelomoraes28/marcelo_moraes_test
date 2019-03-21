from setuptools import setup


extras_require = {
    'test': [
        'pytest==4.2.1',
    ],
}

with open('README.md') as f:
    long_description = f.read()

setup(
    name='string_lib',
    version='0.0.1',
    description='String Lib',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    author='Marcelo Moraes',
    author_email='marcelomoraesjr28@gmail.com',
    url='https://github.com/marcelomoraes28/ormuco',
    keywords='string stringcompare',
    include_package_data=True,
    zip_safe=False,
    extras_require=extras_require,
    packages=['string_lib']
)
