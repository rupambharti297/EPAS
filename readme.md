# Emergency Priority Allocation System (EPAS)

EPAS is a decision-support prototype that helps traffic authorities
decide the appropriate level of road priority for emergency vehicles
based on urgency and traffic conditions.

## What this prototype does
- Accepts emergency request inputs
- Simulates traffic conditions
- Recommends a graded priority level
- Keeps final decision with human authorities

## What this prototype does NOT do
- It does not control traffic signals automatically
- It does not use real city traffic data
- It does not replace human judgment

## How to run
pip install -r requirements.txt
python3 main.py

# git 
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/rupambharti297/EPAS.git
git push -u origin main