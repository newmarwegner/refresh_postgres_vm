# Refresh materialized views postgres   
Script to be use on refresh materialized views.

## Steps to execute:
1. Open terminal
2. Clone Repo
3. Create a virtualenv   
4. Go into /refresh_vm
5. Copy .env-sample of contrib folder into refresh_vm folder and rename to .env
6. Fill the parameter in .env file   
7. Run main.py

## Codes
```
git clone https://github.com/newmarwegner/refresh_postgres_vm.git
cd /refresh_vm
python -m venv .venv
mv /refresh_vm/contrib/.env-sample .env
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```
