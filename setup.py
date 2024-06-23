from setuptools import find_packages, setup



setup(
    name="financebot",
    version="0.0.1",
    author="Sujata",
    author_email="sujataroy2009@gmail.com",
    packages =find_packages(),
    install_requires=["langchain","langchain-openai","langchain-astradb","datasets","pypdf","python-dotenv","flask"]
)