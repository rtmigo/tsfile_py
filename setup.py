from pathlib import Path

from setuptools import setup, find_packages

readme = (Path(__file__).parent / 'README.md').read_text()

setup(
  name="tsfile",
  version="0.0.0",

  author="Artёm IG",
  author_email="ortemeo@gmail.com",
  #url='https://github.com/rtmigo/flaskrun_py#flaskrun',

  packages=find_packages(),

  description="Finds and parsed the timestamp.txt file",

  long_description=readme,
  long_description_content_type='text/markdown',

  license='MIT',

  classifiers=[
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Operating System :: POSIX",
  ],
)
