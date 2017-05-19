from setuptools import setup

setup(name='stride',
      version='1.0.0',
      description='',
      url='https://github.com/davidemms/STRIDE',
      author='David Emms',
      author_email='david_emms@hotmail.com',
      license='Oxford University academic use licence',
      packages=['stride'],
      zip_safe=False,
      entry_points = {
        'console_scripts': ['stride=stride.stride:main']})

