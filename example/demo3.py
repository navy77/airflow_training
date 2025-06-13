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

name = 'toey'
div = 'mic'
grade = 'F'

def func1(name):
    print(f"my name is {name}")

def func2(name,div):
    print(f"my name is {name} from {div}")

def func3(name,div,grade):
    print(f"my name is {name} from {div},I wish {grade}!!!")

with DAG(
    default_args=default_args,
    dag_id="demo-03",
    description='this DAG for demo training',
    schedule_interval= "@daily",
    start_date = days_ago(1),
    catchup = False

) as dag:
    
    task1 = PythonOperator(
        task_id='task1',
        python_callable=func1,
        op_kwargs={  #op_args={} --> single var  op_kwargs-->dict
            'name':name,
            'div': div,
            'grade': grade
        }
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=func2,
        op_kwargs={
            'name':name,
            'div': div,
            'grade': grade
        }
    )

    task3 = PythonOperator(
        task_id='task3',
        python_callable=func3,
        op_kwargs={
            'name':name,
            'div': div,
            'grade': grade
                }
    )

    # dag flow
task1 >> task2 >> task3
