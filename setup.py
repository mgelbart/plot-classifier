from setuptools import setup

setup(
    name='plot_classifier',
    version='0.1',
    description='Plot scikit-learn classifiers nicely in 2D.',
    author='Mike Gelbart',
    author_email="mgelbart@cs.ubc.ca",
    packages=['plot_classifier'],
    install_requires=['numpy>=1.12', 'matplotlib>=2.1'],
    url='https://github.com/mgelbart/plot-classifier',
    license='BSD 3'
)