from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator,BranchPythonOperator
import random

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

def fun_grade():
    list_grade = ['a', 'b', 'c', 'f']
    grade = random.choice(list_grade)
    return f"task_{grade}"

def a(name,div):
    print(f"my name is {name} from {div},I wish a !!!")

def b(name,div):
    print(f"my name is {name} from {div},I wish b !!!")

def c(name,div):
    print(f"my name is {name} from {div},I wish c !!!")

def f(name,div):
    print(f"my name is {name} from {div},I wish f !!!")


with DAG(
    default_args=default_args,
    dag_id="demo-04",
    description='this DAG for demo training',
    schedule_interval= "@daily",
    start_date = days_ago(1),
    catchup = False

) as dag:
    
    task1 = PythonOperator(
        task_id='task1',
        python_callable=func1,
        op_kwargs={
            'name':name,
        }
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=func2,
        op_kwargs={
            'name':name,
            'div': div
        }
    )

    task_a = PythonOperator(
        task_id='task_a',
        python_callable=a,
        op_kwargs={
            'name':name,
            'div': div
        }
    )

    task_b = PythonOperator(
        task_id='task_b',
        python_callable=b,
        op_kwargs={
            'name':name,
            'div': div
        }
    )
    
    task_c = PythonOperator(
        task_id='task_c',
        python_callable=c,
        op_kwargs={
            'name':name,
            'div': div
        }
    )

    task_f = PythonOperator(
        task_id='task_f',
        python_callable=f,
        op_kwargs={
            'name':name,
            'div': div
        }
    )

    select_grade = BranchPythonOperator(
        task_id='select_grade',
        python_callable = fun_grade,
        provide_context = True
    )
    # dag flow
task1 >> task2 >> select_grade >> [task_a,task_b,task_c,task_f]
