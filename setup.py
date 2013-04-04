from setuptools import setup

setup(name='WanderOpenshift',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask>=0.8','wander'],
      dependency_links=['https://github.com/Ramblurr/wander/tarball/master#egg=wander']
     )
