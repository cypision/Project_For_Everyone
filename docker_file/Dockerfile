FROM ubuntu_python_base:0.0.1

LABEL maintainer="Cheong Jin Hwan"

# jupyter_lab ��ġ && tensorflow 2.0 ��ġ
RUN pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org setuptools --upgrade \
      pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org jupyterlab \
      pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org tensorflow==2.2.0
