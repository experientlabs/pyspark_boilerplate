from etl.utils.common import DotDict, NestedDict

job_params = {
    "paths": {
        "log_dir_name": "/logs/",
        "output_data_path": "../../data/target_data",
        "landing_path": "data/source_data/aa_data/api_landing_data",
        "superman_path": "data/source_data/aa_data/superman",
        "input_path": "resources/data/source_data/aa_data",
        "super_man_url": "https://gitlab.com/im-batman/simple-data-assestment/-/raw/main/superman.json",
        "random_user_url": "https://randomuser.me/api/0.8/?results=100"
    },
    "file_name": {
        "random_user_csv_file": "random_user_data.csv",
        "super_man_json_file":  "superman_final.json",
        "processed_csv": "processed_data.csv"
    },
    "job_parameter": {"aa_data_job": {"steps_per_floor": 21}},
}

