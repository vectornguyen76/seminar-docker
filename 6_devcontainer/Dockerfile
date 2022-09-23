FROM python:3

ARG USERNAME=vectornguyen
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG WORK_DIR=/home/$USERNAME

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --create-home --shell /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME

USER $USERNAME
WORKDIR $WORK_DIR

COPY --chown=$USERNAME . .

COPY requirements.txt $WORK_DIR

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . $WORK_DIR

CMD ["python", "main.py"]