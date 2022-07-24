import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="howtotaskier-ycui",
    version="0.4",
    author="Yong Cui",
    author_email="yong.cui01@gmail.com",
    description="This is a task management app.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ycui1/python_how_to",
    packages=setuptools.find_packages(),
    install_requires = ["streamlit"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)