from setuptools import setup, find_packages

setup(
    name='pyrav4l2',
    version='1.0',
    author='Antmicro Ltd',
    description="Pythonic, Really Awesome V4L2 utility",
    author_email='contact@antmicro.com',
    packages=find_packages(include=["pyrav4l2"]),
    include_package_data=True,
    license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
