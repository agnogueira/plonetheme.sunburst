import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.2.3dev'

long_description = (
    read('README.txt')
    + '\n' +
    read('plonetheme', 'sunburst', 'README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n'
    )

setup(name='plonetheme.sunburst',
      version=version,
      description="The default theme for Plone 4.",
      long_description=long_description,
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
        ],
      keywords='web zope plone theme',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plonetheme.sunburst',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      extras_require={'test': ['collective.testcaselayer']},
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
