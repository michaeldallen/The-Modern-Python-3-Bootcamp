from setuptools import setup

setup(
    name="rps",
    version="1.0",
    ph_modules=["rps"],
    install_requires=[
        "Click",
    ]
    entry_points='''
        [console_scripts]
        rps=rps:cli
    '''
)