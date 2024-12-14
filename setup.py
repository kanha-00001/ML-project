from setuptools import find_packages, setup
from typing import List

Hypen_E = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if Hypen_E in requirements:
            requirements.remove(Hypen_E)

    return requirements

setup(
    name="Ml project",
    version="0.0.1",
    author="kanha",
    author_email="kanhiyagoyal2003@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
