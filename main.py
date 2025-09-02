from module.python.testrail import *
from testrail_client import TestRailClient

def main():
    """Main function to demonstrate TestRail API usage"""
    try:
        print("=== TestRail API Demo Project ===")
        client = TestRailClient()
        print(" Successfully connected to TestRail")
        
        # Get and display projects
        print("\n--- Available Projects ---")
        projects = client.get_projects()["projects"]
        for project in projects:
            print(f"ID: {project['id']}, Name: {project['name']}")
        
        # Get project details
        project_id = client.config.project_id
        project = client.get_project(project_id)
        print(f"\n--- Working with Project: {project['name']} ---")
        
        # Get test cases
        print("\n--- Test Cases ---")
        cases = client.get_cases(project_id)["cases"]
        print(f"Found {len(cases)} test cases")
        
        # Display first few cases
        for case in cases:
            print(f"Case ID: {case['id']}, Title: {case['title']}")
        
        # Get test runs
        print("\n--- Test Runs ---")
        runs = client.get_runs(project_id)["runs"]
        print(f"Found {len(runs)} test runs")
        
        # Display active runs
        active_runs = [run for run in runs if not run['is_completed']]
        print(f"Active runs: {len(active_runs)}")
        
        for run in active_runs[:3]:
            print(f"Run ID: {run['id']}, Name: {run['name']}")
        
        print("\ Demo completed successfully!")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()