import os
import sys
from setuptools import setup, find_packages

__here__ = os.path.dirname(os.path.abspath(__file__))

package_info = dict.fromkeys(["RELEASE", "COMMIT", "VERSION", "NAME"])

for name in package_info:
    with open(os.path.join(__here__, "insights", "client", name)) as f:
        package_info[name] = f.read().strip()

entry_points = {
    'console_scripts': []
}

runtime = set([
    'six',
    'requests'
])

if (sys.version_info < (2, 7)):
    runtime.add('pyyaml>=3.10,<=3.13')
else:
    runtime.add('pyyaml')


def maybe_require(pkg):
    try:
        __import__(pkg)
    except ImportError:
        runtime.add(pkg)


maybe_require("importlib")
maybe_require("argparse")

if __name__ == "__main__":
    # allows for runtime modification of rpm name
    name = os.environ.get("INSIGHTS_CORE_NAME", package_info["NAME"])

    setup(
        name=name,
        version=package_info["VERSION"],
        description="A subpackage of Insights Core, specialized for Insights Client functionality",
        url="https://github.com/redhatinsights/insights-client-egg",
        author="Red Hat, Inc.",
        author_email="insights@redhat.com",
        packages=find_packages(),
        install_requires=list(runtime),
        package_data={'': ['LICENSE']},
        license='Apache 2.0',
        entry_points=entry_points,
        include_package_data=True
    )
