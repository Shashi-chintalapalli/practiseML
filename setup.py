from setuptools import find_packages,setup
from typing import List

HYPEN_DOT_E = '-e .'

def get_requirment(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n"," ") for req in requirments]
        if HYPEN_DOT_E in requirments:
            requirments.remove(HYPEN_DOT_E)
        return requirments

setup(
    name='Practise ML model',
    author_email="shashi.chintalapalli@gamil",
    author="Shashi Kumar reddy",
    packages=find_packages(),
    install_requires=get_requirment('requirments.txt')
)