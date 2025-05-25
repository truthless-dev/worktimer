from invoke import task


@task
def check(c, branch_name: str = None):
    """Validate commit messages"""
    if branch_name is None:
        branch_name = "$(git rev-parse --abbrev-ref HEAD)"
    c.run(f"cz check --rev-range {branch_name}")


@task(default=True)
def commit(c, all: bool = False):
    """Commit changes"""
    cmd = "cz commit" if not all else "cz commit --all"
    c.run(cmd)
