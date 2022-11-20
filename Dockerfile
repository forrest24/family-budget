FROM python:3.10

# set envs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install poetry and apt dependencies
RUN pip install -U pip \
    && apt update \
    && apt install -y curl netcat gettext \
    && curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"

# install pip dependencies
WORKDIR /code
ENV POETRY_VIRTUALENVS_CREATE false
ADD poetry.lock /code/poetry.lock
ADD pyproject.toml /code/pyproject.toml
RUN --mount=type=cache,target=/root/.cache/pypoetry poetry install --no-interaction --no-ansi