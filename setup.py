import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Webhooker",
    version="0.1.0",
    author="Fellipe Calleia",
    author_email="fellipe@calleia.com.br",
    description="An out-of-the-box webhooker made to serve all your requests.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/calleia/webhooker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
