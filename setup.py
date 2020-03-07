import setuptools

with open('README.md') as file:
    long_description = file.read()

setuptools.setup(
    name='pythml',
    version='1.0',
    license='MIT',
    description='Create WEB HTML pages in Python.',
    author='Matheus Sena Vasconcelos',
    author_email='sena.matheus14@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/senavs/python-html',
    keywords=['html', 'web-html', 'html-pages', 'pytml', 'python-html', 'pyhtml'],
    packages=['pytml', 'pytml.essential', 'pytml.tags'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_required='>=3.6'
)
