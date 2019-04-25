from setuptools import find_packages, setup

setup(
    name='DTAT_main_server',
    version='0.4.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'requests',
    ],
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'pytest-flask',
        'pytest-mock',
    ],
)