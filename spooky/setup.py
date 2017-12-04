from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

        
setup(name='spooky',
      version='0.1',
      description='package for collaborative Kaggle participation',
      url='https://github.com/ArmandGiraud/spooky',
      author='Armand Giraud',
      author_email='armand.Giraud.ag@gmail.com',
      license='MIT',
      packages=['spooky'],
      install_requires=[
      "sklearn>0.19.1","pandas>0.20.3"
      ]
      zip_safe=False)