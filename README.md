# ContactEngineering Container Stack

A collection of container recipes around the ContactEngineering ecosystem and their build, testing, and publication automatization.

## jupyterlab-SurfaceTopography

[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/imteksim/jupyterlab-surfacetopography?label=dockerhub)](https://hub.docker.com/repository/docker/imteksim/jupyterlab-surfacetopography) [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ContactEngineering/ce-container-stack/build-and-test)](https://github.com/ContactEngineering/ce-container-stack/actions?query=workflow%3Abuild-and-test)

This docker image bases on the [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/)
and provides the core `SurfaceTopography` package and a few other satellite packages from the 
`ContactEngineering` ecosystem. The image works both with

    docker run -p 8888:8888 imteksim/jupyterlab-surfacetopography:latest

and

    singularity run docker://imteksim/jupyterlab-surfacetopography:latest

Please see the [docker/jupyterlab-SurfaceTopography/README.md](docker/jupyterlab-SurfaceTopography/README.md) for more information.
