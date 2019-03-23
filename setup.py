from setuptools import find_packages, setup

setup(
    name='DTAT - main server',
    version='0.2.0',
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
    ],
)