from invoke import Collection

from . import (
    dependencies,
    documentation,
    formatting,
    tests,
)


ns = Collection()
ns.add_collection(documentation, name="docs")
ns.add_collection(formatting, name="fmt")
ns.add_collection(tests, name="test")
ns.add_task(dependencies.install_all)
