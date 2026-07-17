from airflow.decorators import dag, task
import pendulum
from raw.cost.cost_axon import get_report_data

@dag(
    schedule="30 7 * * *", # run at 14h30 everyday
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    tags=["learning"]
)
def hello_airflow_dag():
    
    @task
    def say_hello():
        print("hello!", flush=True)
        
    @task
    def get_report_data_from_app():
        print("Getting report....")
        get_report_data()
  
    t1 = say_hello()
    t2 = get_report_data_from_app()
    t1 >> t2

hello_airflow_dag()