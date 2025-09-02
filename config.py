import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class to manage TestRail settings"""
    
    def __init__(self):
        # Get TestRail connection details from environment variables
        self.testrail_url = os.getenv('TESTRAIL_URL')
        self.testrail_email = os.getenv('TESTRAIL_EMAIL')
        self.testrail_api_key = os.getenv('TESTRAIL_API_KEY')
        
        # Get project settings
        self.project_id = int(os.getenv('PROJECT_ID', 1))
        self.suite_id = int(os.getenv('SUITE_ID', 1))
        
        # Check if all required settings are present
        self._validate_config()
    
    def _validate_config(self):
        """Check if all required configuration values are set"""
        required_fields = [
            ('TESTRAIL_URL', self.testrail_url),
            ('TESTRAIL_EMAIL', self.testrail_email),
            ('TESTRAIL_API_KEY', self.testrail_api_key)
        ]
        
        missing_fields = []
        for field_name, field_value in required_fields:
            if not field_value:
                missing_fields.append(field_name)
        
        if missing_fields:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_fields)}")
    
    def get_auth_tuple(self):
        """Return authentication tuple for requests"""
        return (self.testrail_email, self.testrail_api_key)