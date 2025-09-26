import json

def generate_data():
    """Generates synthetic user data and saves it to a JSON file."""
    data = {
        "users": {
            "user_101": {
                "name": "Python Developer",
                "preferences": ["python", "api", "backend", "performance", "docker"]
            },
            "user_102": {
                "name": "Data Analyst",
                "preferences": ["pandas", "sql", "statistics", "visualization", "matplotlib"]
            }
        },
        "queries": [
            {
                "user_id": "user_101",
                "original_query": "how to read a file",
                "ground_truth_rewrite": "how to read a file in python with performance in mind"
            },
            {
                "user_id": "user_101",
                "original_query": "best way to build a web service",
                "ground_truth_rewrite": "best way to build a python backend api with docker"
            },
            {
                "user_id": "user_102",
                "original_query": "clean up my dataset",
                "ground_truth_rewrite": "how to clean up a dataset using pandas"
            },
            {
                "user_id": "user_102",
                "original_query": "show trends in sales data",
                "ground_truth_rewrite": "how to show trends in sales data with matplotlib visualization"
            },
            # Add 50-200 queries to be thorough
        ]
    }

    with open("data/synthetic_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Synthetic data generated in data/synthetic_data.json")

if __name__ == '__main__':
    generate_data()