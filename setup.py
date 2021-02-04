import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skyscrapers",
    version="0.0.1",
    author="Yuliia Maksymyuk",
    author_email="yuliia.maksymyuk@ucu.edu.ua",
    description="solution of the first task of the first programming lab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juliaaz/skyscrapers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)