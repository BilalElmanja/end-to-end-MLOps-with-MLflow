import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mlProject", # Replace with your own username
    version="0.0.1",
    author="EL MANJA BILAL",
    author_email="elmanjabilal@gmail.com",
    description="A small package for ml project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BilalElmanja/end-to-end-MLOps-with-MLflow", # Replace with your github repo
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

)