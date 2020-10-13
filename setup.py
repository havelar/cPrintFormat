import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cPrintFormat",
    version="0.1.3",
    author="Henrique Avelar Amaral",
    author_email="henrique200297@gmail.com",
    description="Function and Class to easy print colored.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/havelar/cprint",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)