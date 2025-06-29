from setuptools import setup, find_packages

setup(
    name="generate_fake_code_image",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'generate_fake_code_image = src.main:main',
        ],
    },
)
