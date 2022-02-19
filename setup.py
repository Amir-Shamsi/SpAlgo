from setuptools import find_packages, setup

setup(
    name='SpAlgo',
    packages=find_packages(include=['SpAlgo']),

    version='0.1.0',
    description='SpAlgo is a python library with special algorithms which will helps you in your education and your tasks.',
    author='Mohammad Keshavarzi & Amir Shamsi',
    url='https://github.com/Amir-Shamsi/SpAlgo',

    license='MIT',
    author_email='amirshamsi.github@gmail.com',

    github='https://github.com/mohammadkeshavarzi/SpAlgo & https://github.com/Amir-Shamsi',
    linkedin='https://linkedin.com/in/amir-shamsi & https://linkedin.com/in/mohammad-keshavarzi-1b1671218',

    install_requires=[
        'math',
        'operator'
    ],
    download_url='https://github.com/Amir-Shamsi/SpAlgo/archive/refs/tags/0.1.0.tar.gz',

    keywords=['SpAlgo', 'Algorithm', 'Matrix', 'Array'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
