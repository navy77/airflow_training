from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator,BranchPythonOperator
from airflow.providers.http.hooks.http import HttpHook
import json

default_args = {
    'owner': 'mic/iot_team',
    'depends_on_past': False, # f=not run task until pass
    'retries':2,
    'retry_delay':timedelta(minutes=0.05),
}


# https://catfact.ninja/fact
def fetch_data(**kwargs):  
    http = HttpHook(http_conn_id='api_demo',method='GET')
    response = http.run(endpoint='fact')
    data = response.json()
    print(data)
    
with DAG(
    default_args=default_args,
    dag_id="demo-07",
    description='this DAG for demo training',
    schedule_interval= "@daily",
    start_date = days_ago(1),
    catchup = False

) as dag:
    task_api = PythonOperator(
        task_id='task_api',
        python_callable=fetch_data
    )

# dag flow
task_api 