from setuptools import find_packages, setup

setup(
    name='SpAlgo',
    packages=find_packages(include=['SpAlgo']),

    version='0.1.0',
    description='SpAlgo has some special algorithms to help you in your education and your tasks.',
    author='Amir Shamsi',
    url='https://github.com/Amir-Shamsi/SpAlgo',

    license='MIT',

    github='https://github.com/Amir-Shamsi',
    linkedin='https://linkedin.com/in/amir-shamsi',

    install_requires=[],

    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)