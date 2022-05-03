from setuptools import find_packages, setup


setup(
    name='tomek',
    packages=find_packages(),
    include_package_data=True,
    version='0.1',
    description='Need more Tomek in your Django?',
    author='Marc Tamlyn',
    author_email='marc.tamlyn@gmail.com',
    url='https://github.com/mjtamlyn/tomek',
    license='BSD',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
