import os
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

# Below function is used to get all the requirements in requiremts.txt 
# into a list requirements, by removing hype e dot form the list

def get_requirements(file_path:str) ->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='Indian house price analysis',
    version='0.0.1',
    author='Nikhil Reddy 84',
    author_email="nikhilreddyaleti2002@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)