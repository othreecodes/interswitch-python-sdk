from setuptools import setup, find_packages

setup(name='interswitch-python-sdk',
      version='0.1',
      description='Interswitch sdk',
      long_description='Interswitch sdk',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Text Processing :: Linguistic',
      ],
      keywords='Interswitch',
      url='http://github.com/othreecodes/interswitch-python-sdk',
      author='Obi Uchenna David',
      author_email='daviduchenna@outlook.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'requests',
          'pytest'
      ],
      include_package_data=True,
      zip_safe=False)
