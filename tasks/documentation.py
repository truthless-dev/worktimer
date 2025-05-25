import os

from invoke import task


DIR_BASE = "docs"
DIR_BUILD = os.path.join(DIR_BASE, "_build")
DIR_HTML = os.path.join(DIR_BUILD, "html")


@task
def clean(c):
    """Remove previous docs builds"""
    c.run(f"rm -rf {DIR_BUILD}")


@task(
    name="html",
    pre=(clean,),
    default=True,
)
def build_html(c):
    """Build HTML docs"""
    c.run(f"sphinx-build -b html {DIR_BASE} {DIR_HTML}")
