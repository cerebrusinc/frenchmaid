import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="frenchmaid",
    version="0.1.1",
    description="Remove all pests from your project! frenchmaid is a lightweight all platform cli package that will delete all __pycache__ folders (contents included) in your project directory. Are you tired of doing it manually each time? Fear not, the frenchmaid will do it for you!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lewisjr/frenchmaid.git",
    project_urls={
        "Bug Tracker": "https://github.com/lewisjr/frenchmaid/issues",
    },
    author = "Techtronics Solutions Limited | Lewis Mosho Jr",
    author_email = "lmosho@techtronicsltd.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    packages=["frenchmaid"],
    include_package_data=True,
    install_requires=["click", "colorama", "typer"],
    entry_points={
        "console_scripts": [
            "frenchmaid=frenchmaid.__main__:main",
        ]
    },
    package_dir={"": "src"},
    python_requires=">=3.0",
)