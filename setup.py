from setuptools import setup, find_packages

setup(
    name='multilayerGM',
    description='Generate multilayer networks with mesoscale structure',
    url='https://github.com/MultilayerGM/MultilayerGM-py',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author='Lucas G. S. Jeub',
    python_requires='>=3.5',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'nxMultilayerNet @ git+https://github.com/LJeub/nxMultilayerNet.git'
    ],
)
