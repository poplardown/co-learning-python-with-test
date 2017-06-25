from setuptools import setup

setup(
    name='lev',
    packages=['lev'],
    include_package_data=True,
    install_requires=[
        'editdistance',
        'python-Levenshtein',
        'pylev',
        'pyxdameraulevenshtein',
    ],
)

# vim: expandtab
