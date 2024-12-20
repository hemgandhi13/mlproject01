from setuptools import find_packages, setup
from typing import List



HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    This function reads the requirements file and returns a list of requirements
    '''
    requirements = []
    with open(file_path, "r") as file:
        for line in file:
            requirements.append(line.strip())
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = "mlproject01",
    version = "0.1",
    author = "Hem Gandhi",
    author_email = "hemgandhigithub13@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)