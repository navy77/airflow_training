from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator,BranchPythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
import json

default_args = {
    'owner': 'mic/iot_team',
    'depends_on_past': False, # f=not run task until pass
    'retries':2,
    'retry_delay':timedelta(minutes=0.05),
}

with DAG(
    default_args=default_args,
    dag_id="demo-07",
    description='this DAG for demo training',
    schedule_interval= "@daily",
    start_date = days_ago(1),
    catchup = False

) as dag:
    task_api = SimpleHttpOperator(
        task_id='task_api',
        endpoint='https://catfact.ninja/fact',
        http_conn_id="api_http",
        method="GET",
        response_filter=lambda response: json.load(response.text),
        log_response = True
    )

# dag flow
task_api 