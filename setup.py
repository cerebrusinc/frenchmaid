import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="frenchmaid",
    version="0.2.0",
    description="Remove all pests from your project! frenchmaid is a lightweight all platform cli package that will delete all pycache and other folders (contents included) in your project directory. Are you tired of doing it manually each time? Fear not, the frenchmaid will do it for you!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lewisjr/frenchmaid.git",
    project_urls={
        "Bug Tracker": "https://github.com/lewisjr/frenchmaid/issues",
    },
    author = "Techtronics Solutions Limited | Lewis Mosho Jr",
    author_email = "lmosho@techtronicsltd.com",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Typing :: Typed"
    ],
    packages=["frenchmaid", "frenchmaid.modules", "frenchmaid.switches"],
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