FROM continuumio/miniconda3:25.1.1-2

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY environment.yml ./environment.yml
RUN conda env create -f environment.yml \
    && conda clean --all --yes

COPY requirements.txt ./requirements.txt
RUN conda run --no-capture-output -n jupyterlab pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8888

CMD ["conda", "run", "--no-capture-output", "-n", "jupyterlab", "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--ServerApp.root_dir=/workspace", "--ServerApp.token="]