# FINDING GEMS
### Let's play a game! Finding gems (Food Trucks) across San Francisco.
### Select your game difficulty:
- Easy - you will have more tries to find gems and Hard - you will have less opportunities
- After picking a place by entering a latitude and longitude your score will be higher if the place you chose is more food truck dense :).
- Have fun! To play this exciting game you will need:   
#### Create Virtual env and activate
- python -m venv gems_venv
- . .gems_venv/bin/activate
#### Clone Project & Install Requirements
- git clone https://github.com/gmeda-dev/finding-gems.git
- pip install -r requirements.txt
#### Migrate & Run Server
- ./manage.py migrate
- ./manage.py runserver