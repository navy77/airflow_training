from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago

from airflow.operators.empty import EmptyOperator

default_args = {
    'owner': 'Van',
    'depends_on_past': False, # f=not run task until pass
    'retries':2,
    'retry_delay':timedelta(minutes=0.05),
}
### Start1 #########  DAG Setting  ###########################################
with DAG(
    default_args=default_args,
    dag_id="demo-01",
    description='this DAG for demo training',
    schedule_interval= "@daily",
    start_date = days_ago(1),
    catchup = False

) as dag:
### End1 #####################################################################

### Start2 #########  TASK Setting  ###########################################
    task1 = EmptyOperator(
        task_id='task1',
    )

    task2 = EmptyOperator(
        task_id='task2',
    )

    task3 = EmptyOperator(
        task_id='task3',
    )
### End2 #####################################################################

### Start3 #########  FLOW SETTING  ###########################################
    # dag flow
task1 >> task2 >> task3
### End3 ######################################################################