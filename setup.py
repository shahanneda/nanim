import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="nanim", # Replace with your own username
        version="0.0.1",
        author="Shahan Neda",
        author_email="shahan.neda@gmail.com",
        description="A python animation library",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/shahanneda/nanim",
        packages=setuptools.find_packages(),
        python_requires='>=3.6',
        entry_points = {
            'console_scripts': [
                'nanim = nanim.nanim:main'
            ]
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
)
