from invoke import Collection

from . import (
    commits,
    dependencies,
    documentation,
    formatting,
    tests,
)


ns = Collection()
ns.add_collection(commits, name="c")
ns.add_collection(documentation, name="docs")
ns.add_collection(formatting, name="fmt")
ns.add_collection(tests, name="test")
ns.add_task(dependencies.install_all)
