from setuptools import setup
import sys

# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# release markers:
#   X.Y
#   X.Y.Z   # For bugfix releases
#
# pre-release markers:
#   X.YaN   # Alpha release
#   X.YbN   # Beta release
#   X.YrcN  # Release Candidate
#   X.Y     # Final release

# make pytest-runner a conditional requirement,
# per: https://github.com/pytest-dev/pytest-runner#considerations

with open("requirements.txt") as f_requirements:
    install_requires = [xx for xx in [x.strip() for x in f_requirements.read().split("\n")] if not xx.startswith("#") and len(xx)>0]

setup(name='screenpy',
      version="0.1",
      description='Parsing screen scripts',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
      keywords='screenpy screenplay parsing',
      url='https://github.com/tbmihailov/ScreenPy/',
      author='-',
      author_email='-',
      license='Apache',
      install_requires=install_requires,
      scripts=["bin/allennlp"],
      setup_requires=install_requires,
      include_package_data=True,
      python_requires='>=3.6.1',
      zip_safe=False)