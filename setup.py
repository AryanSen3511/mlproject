from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    ''' 
    requirements=[]
    with open(file_path , encoding="utf-8") as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(

    name='mlproject',
    version='0.0.1',
    author='Aryan Sen',
    author_email = 'senaryan973@gmail.com',
    packeges=find_packages(),
    # install_requires=['pandas','numpy'] ---> ther will be scenario wherein we have 
    # need multiple packages for that we use create a function it take all function which is required
    install_requires=get_requirements('requirements.txt')
)