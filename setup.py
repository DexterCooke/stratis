from setuptools import setup

setup(
    name="stratis",
    version='1.0',
    py_modules=['stratis_cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        stratis=stratis_cli:cli
    ''',
)