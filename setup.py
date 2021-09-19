from setuptools import setup

setup(name='counsyl-dh-poetry',
      version='0.3.0',
      description='Shim between dh-virtualenv and poetry',
      url='http://github.com/rgoncalves77/dh-poetry',
      author='Rafael Gonçalves',
      author_email='rgoncalves@gmail.com',
      zip_safe=False,
      license="MIT",
      packages=['dh_poetry'],
      entry_points={
          'console_scripts': ['dh-poetry=dh_poetry.command_line:main'],
      },
)
