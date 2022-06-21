from setuptools import setup, find_packages

setup(
    name='Tennis_probability_project',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "absl-py==0.7.1",
        "astor==0.8.0",
        "Click==7.0",
        "Flask==1.0.3",
        "gast==0.2.2",
        "grpcio==1.20.1",
        "h5py==2.9.0",
        "itsdangerous==1.1.0",
        "Jinja2==2.10.1",
        "Keras==2.2.4",
        "Keras-Applications==1.0.7",
        "Keras-Preprocessing==1.0.9",
        "Markdown==3.1.1",
        "MarkupSafe==1.1.1",
        "mock==3.0.5",
        "numpy==1.22.0",
        "pandas==0.24.2",
        "protobuf==3.7.1",
        "python-dateutil==2.8.0",
        "pytz==2019.1",
        "PyYAML==5.1",
        "scipy==1.3.0",
        "six==1.12.0",
        "tensorboard==1.13.1",
        "tensorflow==1.13.1",
        "tensorflow-estimator==1.13.0",
        "termcolor==1.1.0",
        "Werkzeug==0.15.4"
    ],
    description='Predict the tennis match outcome.'
)
