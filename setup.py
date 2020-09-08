from setuptools import setup

requirements = [
    "aiohttp",
    "aiofiles"
]

setup(
    name='apiimgbb',
    version='1.0',
    description="lib for Imgbb",
    author="dark0ghost",
    url='https://github.com/dark0ghost/api_imgbb_aio_python',
    include_package_data=True,
    install_requires=requirements,
    license="MIT License",
    zip_safe=False,
    classifiers=[
        'Natural Language :: English',
    ],
)
