from setuptools import setup

setup(name='dh-poetry',
      version='0.1.1',
      description='Shim between dh-virtualenv and poetry',
      url='http://github.com/michael-christen/dh-poetry',
      author='Michael Christen',
      author_email='mchristen96@gmail.com',
      license='MIT',
      zip_safe=False,
      packages=['dh_poetry'],
      entry_points={
          'console_scripts': ['dh-poetry=dh_poetry.command_line:main'],
      },
)
