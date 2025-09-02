import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from testrail_client import TestRailClient

def demonstrate_basic_operations():
    """Show basic TestRail operations"""
    
    client = TestRailClient()
    project_id = client.config.project_id
    
    print(" Basic TestRail Operations ")
    
    # Get project information
    project = client.get_project(project_id)
    print(f"Project: {project['name']}")
    print(f"URL: {project['url']}")
    
    # Get users
    users = client.get_users()
    print(f"\nTotal users: {len(users)}")
    
    # Get sections
    sections = client.get_sections(project_id)
    print(f"Total sections: {len(sections)}")
    
    # Get milestones
    milestones = client.get_milestones(project_id)
    print(f"Total milestones: {len(milestones)}")

if __name__ == "__main__":
    demonstrate_basic_operations()