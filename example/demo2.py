from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago

from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'mic/iot_team',
    'depends_on_past': False, # f=not run task until pass
    'retries':2,
    'retry_delay':timedelta(minutes=0.05),
}

def func1():
    print("from function 1!!!")

def func2():
    print("from function 2!!!")

def func3():
    print("from function 3!!!")

with DAG(
    default_args=default_args,
    dag_id="demo-02",
    description='this DAG for demo training',
    schedule_interval= "@daily",
    start_date = days_ago(1),
    catchup = False

) as dag:
    
    task1 = PythonOperator(
        task_id='task1',
        python_callable=func1
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=func2
    )

    task3 = PythonOperator(
        task_id='task3',
        python_callable=func3
    )

    # dag flow
task1 >> task2 >> task3
