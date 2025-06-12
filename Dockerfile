FROM apache/airflow:2.10.5-python3.9

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY dags/ /opt/airflow/dags/

COPY entrypoint.sh /entrypoint.sh

USER root

RUN sed -i 's/\r$//' /entrypoint.sh && chmod +x /entrypoint.sh

USER airflow

ENTRYPOINT ["/entrypoint.sh"]