import setuptools
try:
    import pkg_utils
except ImportError:
    import pip._internal
    pip._internal.main(['install', 'pkg_utils'])
    import pkg_utils
import os

name = 'portfolio_tools'
dirname = os.path.dirname(__file__)
package_data = {
    name: [
        'VERSION',
    ],
}

# get package metadata
md = pkg_utils.get_package_metadata(
    dirname, name, package_data_filename_patterns=package_data)

# install package
setuptools.setup(
    name=name,
    version=md.version,
    description='A package to query and format the data in the integrated Datanator database',
    long_description=md.long_description,
    author="Zhouyang Lian",
    author_email="zhouyang.lian@familian.life",
    license="MIT",
    keywords='',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    package_data=md.package_data,
    install_requires=md.install_requires,
    extras_require=md.extras_require,
    tests_require=md.tests_require,
    dependency_links=md.dependency_links,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)