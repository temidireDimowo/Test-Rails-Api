import requests
import json
from config import Config

class TestRailClient:
    """Main client class for interacting with TestRail API"""
    
    def __init__(self):
        # Initialize configuration
        self.config = Config()
        self.base_url = f"{self.config.testrail_url}/index.php?/api/v2"
        self.auth = self.config.get_auth_tuple()
        
        # Set up request headers
        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'TestRail Python Client'
        }
    
    def _make_request(self, method, endpoint, data=None):
        """Make HTTP request to TestRail API"""
        url = f"{self.base_url}/{endpoint}"
        
        try:
            if method.upper() == 'GET':
                response = requests.get(url, auth=self.auth, headers=self.headers)
            elif method.upper() == 'POST':
                response = requests.post(
                    url, 
                    auth=self.auth, 
                    headers=self.headers,
                    data=json.dumps(data) if data else None
                )
            elif method.upper() == 'PUT':
                response = requests.put(
                    url,
                    auth=self.auth,
                    headers=self.headers,
                    data=json.dumps(data) if data else None
                )
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            # Check if request was successful
            response.raise_for_status()
            
            # Return JSON response if available
            if response.content:
                return response.json()
            return None
            
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response status: {e.response.status_code}")
                print(f"Response content: {e.response.text}")
            raise
    
    # Project methods
    def get_projects(self):
        """Get all projects from TestRail"""
        return self._make_request('GET', 'get_projects')
    
    def get_project(self, project_id):
        """Get specific project by ID"""
        return self._make_request('GET', f'get_project/{project_id}')
    
    # Test case methods
    def get_cases(self, project_id, suite_id=None):
        """Get test cases from a project"""
        endpoint = f'get_cases/{project_id}'
        if suite_id:
            endpoint += f'&suite_id={suite_id}'
        return self._make_request('GET', endpoint)
    
    def get_case(self, case_id):
        """Get specific test case by ID"""
        return self._make_request('GET', f'get_case/{case_id}')
    
    def add_case(self, section_id, title, **kwargs):
        """Add new test case to a section"""
        data = {
            'title': title,
            **kwargs
        }
        return self._make_request('POST', f'add_case/{section_id}', data)
    
    def update_case(self, case_id, **kwargs):
        """Update existing test case"""
        return self._make_request('POST', f'update_case/{case_id}', kwargs)
    
    # Test run methods
    def get_runs(self, project_id):
        """Get all test runs for a project"""
        return self._make_request('GET', f'get_runs/{project_id}')
    
    def get_run(self, run_id):
        """Get specific test run by ID"""
        return self._make_request('GET', f'get_run/{run_id}')
    
    def add_run(self, project_id, name, **kwargs):
        """Create new test run"""
        data = {
            'name': name,
            **kwargs
        }
        return self._make_request('POST', f'add_run/{project_id}', data)
    
    def close_run(self, run_id):
        """Close a test run"""
        return self._make_request('POST', f'close_run/{run_id}')
    
    # Test result methods
    def get_results_for_case(self, run_id, case_id):
        """Get test results for a specific case in a run"""
        return self._make_request('GET', f'get_results_for_case/{run_id}/{case_id}')
    
    def add_result_for_case(self, run_id, case_id, status_id, **kwargs):
        """Add test result for a specific case"""
        data = {
            'status_id': status_id,
            **kwargs
        }
        return self._make_request('POST', f'add_result_for_case/{run_id}/{case_id}', data)
    
    def add_results_for_cases(self, run_id, results):
        """Add multiple test results at once"""
        data = {'results': results}
        return self._make_request('POST', f'add_results_for_cases/{run_id}', data)
    
    # Milestone methods
    def get_milestones(self, project_id):
        """Get all milestones for a project"""
        return self._make_request('GET', f'get_milestones/{project_id}')
    
    def add_milestone(self, project_id, name, **kwargs):
        """Add new milestone"""
        data = {
            'name': name,
            **kwargs
        }
        return self._make_request('POST', f'add_milestone/{project_id}', data)
    
    # Section methods
    def get_sections(self, project_id, suite_id=None):
        """Get sections from a project"""
        endpoint = f'get_sections/{project_id}'
        if suite_id:
            endpoint += f'&suite_id={suite_id}'
        return self._make_request('GET', endpoint)
    
    def add_section(self, project_id, name, **kwargs):
        """Add new section"""
        data = {
            'name': name,
            **kwargs
        }
        return self._make_request('POST', f'add_section/{project_id}', data)
    
    # User methods
    def get_users(self):
        """Get all users"""
        return self._make_request('GET', 'get_users')
    
    def get_user(self, user_id):
        """Get specific user by ID"""
        return self._make_request('GET', f'get_user/{user_id}')