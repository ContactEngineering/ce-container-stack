# Build from within repository root 
#
# Modify conda enviornment running jupyter notebooks
FROM jupyter/minimal-notebook:python-3.11.5

USER root

# FROM imkteksim/dtool-jupyter:latest
# Install from requirements.txt file
RUN apt-get --yes update && \
    apt-get --yes install \
        clang cmake curl g++ gdb git m4 wget \
        libboost-test-dev \ 
        libcurl4-openssl-dev \
        libeigen3-dev \
        libfftw3-dev \
        libgmp-dev \
        libnetcdf-dev \
        libopenblas-base \
        libopenblas-dev \
        python3-pip \
        python3-dev \
        python3-netcdf4 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --chown=${NB_UID}:${NB_GID} jupyterlab-SurfaceTopography/conda-requirements.in "/home/${NB_USER}/"
RUN pip install pip-tools
RUN pip-compile "/home/${NB_USER}/conda-requirements.in" > "/home/${NB_USER}/conda-requirements.txt"
RUN pip install --quiet --no-cache-dir --requirement "/home/${NB_USER}/conda-requirements.txt" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Workaround for building packages and introducing an ipykernel outside of the jupyterlab conda environment
RUN PATH=$(echo "$PATH" | sed -e 's|/opt/conda[^:]*:||g') && ( \
        pip install meson ninja && \
        pip install ipykernel && \
        python3 -m ipykernel install --name SurfaceTopography --display-name "Python (SurfaceTopography)") && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Workaround for modifying system python outside of the jupyterlab conda environment
COPY --chown=${NB_UID}:${NB_GID} jupyterlab-SurfaceTopography/requirements.txt "/home/${NB_USER}/"
RUN PATH="$(echo "$PATH" | sed -e 's|/opt/conda[^:]*:||g')" && ( \
        pip install --quiet --no-cache-dir --requirement "/home/${NB_USER}/requirements.txt" )

COPY jupyterlab-SurfaceTopography/start-wrapper.sh /usr/local/bin/

# Custom fonts config
COPY jupyterlab-SurfaceTopography/etc/fonts.conf /etc/fonts/conf.avail/99-injected.conf
RUN ln -s /etc/fonts/conf.avail/99-injected.conf /etc/fonts/conf.d/99-injected.conf
RUN mkdir -p /fonts

# Install from requirements.txt file
RUN apt-get --yes update && \
    apt-get --yes install fontconfig && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /home/${NB_USER}/work
USER ${NB_UID}

# Remove annoying conda environment from terminal sessions
RUN echo "conda deactivate" >> "${HOME}/.bashrc"
RUN echo 'export PATH=$(echo "$PATH" | sed -e '"'"'s|/opt/conda[^:]*:||g'"'"')' >> "${HOME}/.bashrc"

# Set default kernel
RUN echo "c.MultiKernelManager.default_kernel_name = 'surfacetopography'" >> "${HOME}/.jupyter/jupyter_server_config.py"

# Copy jupyter-app-launcher configuration
ENV JUPYTER_APP_LAUNCHER_PATH="/home/${NB_USER}/.jupyter/jupyter_app_launcher"
COPY --chown=${NB_UID}:${NB_GID} jupyterlab-SurfaceTopography/etc/jupyter_app_launcher "/home/${NB_USER}/.jupyter/jupyter_app_launcher"

# Copy README.md
COPY --chown=${NB_UID}:${NB_GID} jupyterlab-SurfaceTopography/README.md "/home/${NB_USER}/README.md"
RUN pandoc "/home/${NB_USER}/README.md" -o "/home/${NB_USER}/README.html"
RUN md2nb "/home/${NB_USER}/README.md"

CMD ["start-wrapper.sh", "start-notebook.sh"]
