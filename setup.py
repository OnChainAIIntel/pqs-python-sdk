from setuptools import setup, find_packages

setup(
    name="pqs-sdk",
    version="0.1.1",
    description="The world's first named AI prompt quality score — Python SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="OnChainIntel",
    author_email="john@onchainintel.net",
    url="https://pqs.onchainintel.net",
    project_urls={
        "GitHub": "https://github.com/OnChainAIIntel/pqs-python-sdk",
        "Documentation": "https://pqs.onchainintel.net",
    },
    packages=find_packages(),
    install_requires=["requests>=2.28.0"],
    python_requires=">=3.8",
    license="MIT",
    keywords=["prompt", "quality", "score", "llm", "ai", "pqs", "x402", "langchain", "crewai", "autogen"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
