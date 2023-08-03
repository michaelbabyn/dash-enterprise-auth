import io
from setuptools import setup

main_ns = {}
exec(open("dash_enterprise_auth/version.py").read(), main_ns)  # pylint: disable=exec-used

setup(
    name="dash_enterprise_auth",
    version=main_ns["__version__"],
    description="Authentication integrations for apps using Dash Enterprise",
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="dash dash-enterprise dash-auth plotly",
    author="Antoine Roy-Gobeil",
    author_email="antoine@plotly.com",
    license="MIT",
    packages=[
        "dash_enterprise_auth"
    ],
    install_requires=[
        "dash",
        "requests[security]",
        "retrying",
        "PyJWT",
        "cryptography"
    ],
    python_requires=">=3.6",
    url="https://plotly.com/dash",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ]
)
