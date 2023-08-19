FROM python:3.11-bullseye

ENV PYTHONPATH "/app"
ENV PATH="${PATH}:/root/.poetry/bin"
ENV PATH /home/${USERNAME}/.local/bin:${PATH}

WORKDIR /app
RUN pip install poetry && mkdir ./src && touch ./src/a.py
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install

COPY src /app/src

RUN mkdir /docker
COPY docker/wallet/entrypoint.sh /docker/wallet-entrypoint.sh
RUN chmod +x /docker/wallet-entrypoint.sh

#CMD alembic upgrade head
ENTRYPOINT ["/docker/wallet-entrypoint.sh"]
#ENTRYPOINT ["uvicorn", "src.apps.rest_api.entrypoint:app", "--reload"]
#COPY requirements.txt /app/src
#RUN pip install -r src/habit_tracker/third_party/requirements.txt
