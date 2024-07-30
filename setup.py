import setuptools
setuptools.setup(
    name='Autoformer', version='0.1',
    packages=setuptools.find_packages(),
    install_requires = ['pandas', 'scikit-learn', 'torchvision', 'numpy < 2.0', 'matplotlib', 'reformer_pytorch'],
    extras_require={'testing': ['pytest']},
)