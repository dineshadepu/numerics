from setuptools import find_packages, setup
from setuptools_rust import Binding, RustExtension


setup_requires = ['setuptools-rust>=0.10.2']
install_requires = ['numpy']
test_requires = install_requires + ['pytest']

setup(
    name='numerics',
    version='0.1.0',
    description='Numerical analysis in python',
    rust_extensions=[
        RustExtension('numerics.math', './Cargo.toml',  binding=Binding.PyO3),
        # RustExtension('autopy.bitmap', 'Cargo.toml', binding=Binding.PyO3),
        # RustExtension('autopy.color', 'Cargo.toml', binding=Binding.PyO3),
        # RustExtension('autopy.key', 'Cargo.toml', binding=Binding.PyO3),
    ],
    install_requires=install_requires,
    setup_requires=setup_requires,
    test_requires=test_requires,
    packages=find_packages(),
    zip_safe=False,
)
