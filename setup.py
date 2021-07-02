from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='PJWSTK-Tetris_game',
    version='0.9.96',
    packages=['game'],
    url='https://github.com/tomaszlemke/Tetris1.0',
    license='MIT',
    author='Tomasz Lemke & Krzysztof Skwira',
    author_email='s19471@pjwstk.edu.pl',
    description='Tetris game',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: pygame",
        "Development Status :: 3 - Alpha",
        "Topic :: Games/Entertainment :: Puzzle Games"
    ],
    install_requires=[
        "pygame ~= 1.9",
    ],
    entry_points={'console_scripts': ['Tetris=game.main:main']}
)
