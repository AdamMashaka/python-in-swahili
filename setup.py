from os import path
from setuptools import setup

# read the contents of your description file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pyswahili",
    version="0.1.4",
    description="""
    Python package for briding python english keywords 
    with swahili one to allow swahili speakers to learn the basics of coding 
    without ever knowing  english 
    """,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Kalebu/pyswahili",
    download_url='https://github.com/Kalebu/pyswahili/releases/tag/0.1',
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["pyswahili"],
    keywords=[
        "pyswahili",
        "python-tanzania",
        "python-transpiler",
        "swahili-python",
        "python in swahili",
        "python for swahili speakers",
        "code python in swahili",
        "swahili programming language",
        "program in swahili",
    ],
    entry_points={
        "console_scripts": [
            "pyswahili = pyswahili.__main__:main"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
