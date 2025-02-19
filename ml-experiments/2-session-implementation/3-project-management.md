# 2 - Project Management
Manage code and dependencies of the Python project for the experiments.

## Versioning

Generally, the entire code (and configuration) should be versioned and tracked with git and GitHub (or similar).

When running an experiment all code (and configuration if applicable) should be referenced by a commit for transparency and reproducibility.
The reference should be [documented](2-documentation.md).

This could look like this:
```bash
# Create a branch for the experiment
git branch experiment-ID

# Make sure everything is committed before starting the experiment
git commit -m "..."

# Get the hash of the current commit
git rev-parse HEAD

# Inspect state later 
git checkout HASH  # undo with: git switch - 
```
**Beware**: If you delete the branch and the commit is not merged to the main branch it may be garbage collected by git.

## Pin dependencies
To reproduce experiments and avoid bugs
- the versions of packages your library depends on should be pinned and
- the version of Python should be pinned,
- the packages should be kept in an isolated virtual environment specific to the project.

Many tools are available for some or all of the tasks (pip, conda, poetry, pipenv, pyenv...). 

We chose `uv` as modern and efficient solution to all of the tasks.

> *Hands-on showcase*



## Structure, Conventions, Tests

Equally important are a clear and well-defined structure of the code, shared conventions when working in teams and tests for crucial parts of the code.
You learned about that in our other sessions.


<!-- 
Maybe: Recommendations for ML experiment specific structure.
 -->