Setting Up a Virtual Environment

Follow the steps below to set up a virtual environment for your project.

1. Creation of Virtual Environment
Replace myenv with the name you desire for your virtual environment.

python3 -m venv myenv

2. Activate the Virtual Environment
For Windows users:

.\myenv\Scripts\activate

For macOS/Linux users:
source myenv/bin/activate

You'll know your virtual environment is activated when you see (myenv) (or your chosen environment name) at the beginning of your command prompt.

3. Install Required Packages
Make sure you have a requirements.txt file in your project directory, then run:

python3 -m pip install -r requirements.txt