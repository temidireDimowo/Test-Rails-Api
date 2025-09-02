import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from testrail_client import TestRailClient
from datetime import datetime

def create_test_run_example():
    """Example of creating and managing test runs"""
    
    client = TestRailClient()
    project_id = client.config.project_id
    suite_id = client.config.suite_id
    
    print(" Test Run Management Example ")
    
    # Create a new test run
    run_name = f"Automated Test Run - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    
    run_data = {
        'suite_id': suite_id,
        'include_all': True,  # Include all test cases
        'description': 'Test run created via Python API'
    }
    
    try:
        new_run = client.add_run(project_id, run_name, **run_data)
        print(f" Created test run: {new_run['name']} (ID: {new_run['id']})")
        
        # Get some test cases to add results
        cases = client.get_cases(project_id, suite_id)
        
        if cases:
            # Add a passing result
            case_id = cases[0]['id']
            result = client.add_result_for_case(
                new_run['id'],
                case_id,
                status_id=1,  # 1 = Passed
                comment="Test passed via API",
                elapsed="5m"
            )
            print(f" Added passing result for case {case_id}")
            
            # Add a failing result if there's another case
            if len(cases) > 1:
                case_id = cases[1]['id']
                result = client.add_result_for_case(
                    new_run['id'],
                    case_id,
                    status_id=5,  # 5 = Failed
                    comment="Test failed - example failure",
                    defects="BUG-123"
                )
                print(f" Added failing result for case {case_id}")
        
        # Close the test run
        client.close_run(new_run['id'])
        print(f" Closed test run {new_run['id']}")
        
    except Exception as e:
        print(f" Error in test run management: {e}")

if __name__ == "__main__":
    create_test_run_example()