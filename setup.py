## responsible for creating our machine laerning application as a package
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
name='mlproject',
version='0.0.1',
author='Gargi',
author_email='gargi.dhulekar23@spit.ac.in',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
)