from setuptools import setup,find_packages
with open("/Users/madewang/PycharmProjects/Input/CiscoSecurityDevice/README.md",'r') as fh:
    long_description = fh.read()
setup(
    name='CiscoSecurityDevice',
    py_modules=['CiscoSecurityDevice'],
    version='0.0.1',
    description='This wrapper is designed to provide a unique interface to interact with ISE and FMC api.',
    author='Madhuri Dewangan',
    author_email='madewang@cisco.com',
    package_dir={'':'CiscoSecurityDevice'},
    classifiers=[
        "Programming Language :: Python 3.7",
        "Operating System :: OS Independent",
        "License :: GNU General Public License v3.0",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests","ISE","fireREST"],

)