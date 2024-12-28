from setuptools import setup, find_packages

# Load the README.md file
with open("README.md", 'r', encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="github-activity",
    version="0.1.0",
    author="VagBal",
    author_email="vagvolgyibalazsrobert@gmail.com",
    description="'A CLI tool to fetch and display recent GitHub activity of a user",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VagBal/github-activity",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.25.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "github-activity=src.main:main"
        ]
    }
)