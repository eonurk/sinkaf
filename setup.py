import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sinkaf", # Replace with your own username
    version="1.0.0",
    author="E Onur Karakaslar",
    author_email="eonurkara@gmail.com",
    description="Türkçe küfürlü içerikleri bulan bir kütüphane",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eonurk/sinkaf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True
)