from setuptools import setup

setup(
    name='mileage',
    version='0.1.0',
    description='A simple fuel efficency calulator',
    #url='',
    author='Geoff English',
    author_email='',
    license='MIT',
    packages=['mileage'],
    scripts=['mileage/mileage_Corolla.py'],
    install_requires = [
      "pandas",
      "numpy",
      "argparse"
      ]
    ),
