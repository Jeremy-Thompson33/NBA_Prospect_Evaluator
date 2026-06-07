NBA Prospect Evaluator

A machine learning project that predicts NBA success for college basketball players using college statistics, combine measurements, and draft data.

Setup
1. Clone the Repository
git clone <repository-url>
cd nba-prospect-evaluator
2. Create and Activate a Virtual Environment

Windows

python -m venv .venv
.venv\Scripts\activate

Mac/Linux

python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt

4. Configure API Credentials

Create a .env file in the project root:

CBBD_API_KEY=your_api_key_here

Get API key here: [collegebasketballdata.com](https://collegebasketballdata.com/key)

The .env file is ignored by Git and should never be committed.

5. Pull Data

Run the data collection scripts to retrieve player statistics and other data sources:
