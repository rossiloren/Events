'''
Main: it searches online events based on the pipeline
'''



import fire
from pipeline import run_pipeline
from config import ConfigEvents

config = ConfigEvents()  # create a single instance of ConfigEvents

if __name__ == "__main__":
    fire.Fire(lambda area, start_date, end_date, output_path: run_pipeline(
        area, start_date, end_date, output_path, config
    ))
