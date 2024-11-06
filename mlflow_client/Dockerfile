FROM continuumio/miniconda3

# Create the environment using conda
RUN conda install -c anaconda jupyter
RUN conda install -c conda-forge mlflow
RUN conda install -c anaconda scikit-learn
RUN conda install -c anaconda psycopg2
RUN conda install -c anaconda boto3
RUN conda install -c cookiecutter xgboost
RUN pip install virtualenv

ENV HOME="/root"
WORKDIR ${HOME}
RUN apt-get update && apt-get install -y curl
RUN apt-get install -y git
RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv
ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"

RUN apt install -y build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev