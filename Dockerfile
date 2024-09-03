FROM apache/airflow:2.2.3

# Instala las dependencias adicionales
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /requirements.txt

# Copia los scripts y DAGs a sus respectivas carpetas en la imagen
COPY dags/ /opt/airflow/dags/
COPY scripts/ /opt/airflow/scripts/

# Inicializa la base de datos
RUN airflow db init
