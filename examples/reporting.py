import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from testrail_client import TestRailClient

def generate_project_report():
    """Generate a simple project report"""
    
    client = TestRailClient()
    project_id = client.config.project_id
    
    print(" TestRail Project Report ")
    
    # Get project details
    project = client.get_project(project_id)
    print(f"Project: {project['name']}")
    print(f"Announcement: {project.get('announcement', 'None')}")
    
    # Get test cases statistics
    cases = client.get_cases(project_id)["cases"]
    print(f"\nTest Cases: {len(cases)}")
    
    # Count cases by priority if available
    priority_counts = {}
    for case in cases:
        priority = case.get('priority_id', 'Unknown')
        priority_counts[priority] = priority_counts.get(priority, 0) + 1
    
    print("Cases by Priority:")
    for priority, count in priority_counts.items():
        print(f"  Priority {priority}: {count}")
    
    # Get test runs statistics
    runs = client.get_runs(project_id)["runs"]
    active_runs = [run for run in runs if not run['is_completed']]
    completed_runs = [run for run in runs if run['is_completed']]
    
    print(f"\nTest Runs:")
    print(f"  Total: {len(runs)}")
    print(f"  Active: {len(active_runs)}")
    print(f"  Completed: {len(completed_runs)}")
    
    # Show recent runs
    print(f"\nRecent Test Runs:")
    for run in runs[:5]:
        status = "Active" if not run['is_completed'] else "Completed"
        print(f"  {run['name']} - {status}")

if __name__ == "__main__":
    generate_project_report()