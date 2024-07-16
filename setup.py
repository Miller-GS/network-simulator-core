from setuptools import setup 
  
setup( 
    name='network_simulator', 
    version='0.1', 
    description='Library with the purpose of simulating a network, virtually implementing protocols used in the Internet', 
    author='Gustavo Miller', 
    packages=['network_simulator'], 
    install_requires=['pytest'],
) 