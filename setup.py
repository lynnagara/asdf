import setuptools  # type: ignore

REQUIREMENTS = [req.strip() for req in open("requirements.txt").readlines()]


setuptools.setup(
    name="asdf",
    packages=setuptools.find_packages(),
    install_requires=REQUIREMENTS,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "cli = asdf.cli:cli",
        ],
    }

)
