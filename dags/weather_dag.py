from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Añadir la ruta del script al PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from weather_script import run_weather_etl

default_args = {
    'owner': 'tu_nombre',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'daily_weather_etl',
    default_args=default_args,
    description='ETL diario de datos meteorológicos desde OpenWeatherMap a Redshift',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 5, 1),
    catchup=False,
) as dag:

    etl_task = PythonOperator(
        task_id='run_weather_etl',
        python_callable=run_weather_etl,
    )

    etl_task
