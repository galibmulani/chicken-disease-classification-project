import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version="0.0.0"

REPO_NAME="chicken-disease-classification-project"
AUTHOR_USER_NAME="galibmulani"
SRC_REPO="cnnClassifier"
AUTHOR_EMAIL="mulanigalib1@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for cnn project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)