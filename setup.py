import codecs
from setuptools import setup, find_packages
from os import path

def read(*parts):
    return codecs.open(path.join(path.dirname(__file__), *parts),
                       encoding="utf-8").read()

setup(name='logstash_handler',
      version='0.1.0',
      description='Log handler meant for logstash',
      long_description=read('README.rst'),
      url='https://github.com/klynch/python-logstash-handler',
      author='Kevin Lynch',
      author_email='klynch@drakontas.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=["logstash_formatter >= 0.5.8"],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3'
      ],
      zip_safe=True)
