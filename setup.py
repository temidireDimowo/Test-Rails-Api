"""
Setup script for TestRail API project
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print(" Requirements installed successfully")

def create_env_file():
    """Create .env file template if it doesn't exist"""
    if not os.path.exists('.env'):
        env_template = """# TestRail connection settings
TESTRAIL_URL=https://your-instance.testrail.io
TESTRAIL_EMAIL=your-email@example.com
TESTRAIL_API_KEY=your-api-key-here

# Project settings
PROJECT_ID=1
SUITE_ID=1
"""
        with open('.env', 'w') as f:
            f.write(env_template)
        print(" Created .env template file")
        print("Please update .env with your TestRail credentials")
    else:
        print(" .env file already exists")

def main():
    """Main setup function"""
    print(" TestRail API Project Setup ")
    
    install_requirements()
    create_env_file()
    
    print("\n Setup Complete ")
    print("Next steps:")
    print("1. Update .env file with your TestRail credentials")
    print("2. Run: python main.py")
    print("3. Try examples: python examples/basic_operations.py")

if __name__ == "__main__":
    main()