[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Pratilipi Connect 4 Game (Under Development)

### Introduction
 
The project provides a central repository for the microservice
which'll be used for interacting with Connect 4 game.
The project is written in Python, with MongoDB as the backbone database and
JSON as interim data layer.
**The project works for the multigame setup and stores game information in the db.**

### Setup

**You can also use the docker file provided instead of creating virtual environment**

Since the project is entirely written in Python, you can use a virtual
environment to keep the dependencies same as the other fellow
developers. A virtual environment can be created/used as follows:

- Using `pip`; install `virtualenv` globally:

        $ sudo pip install virtualenv

- Once `virtualenv` is installed, create a new environment (named
    `user_segmentation`) here:

        $ virtualenv --python=python3 pratilipi
 
- You can manually activate the environment using the following command:

        $ source pratilipi/bin/acivate

- You can exit the environment by simply executing the `deactivate` command:

        $ deactivate



### Deployment

Once you've activated your virtual environment, you no longer need to
use `sudo` to install any dependencies. Simply use the environment's
local copy of `pip` and install all the required packages using the
`requirements.txt` file bundled along with the project:

    $ pip install -r requirements.txt

The above command shall read the dependencies from the
`requirements.txt` file line-by-line, and install the same version as
mentioned in the file. If you're using a new module for your project,
and want to add that to the `requirements.txt` list, simply use a
`freeze` command, and redirect the output to the file.

    $ pip freeze > requirements.txt

Simply run:

    $ python app.py
    
The service runs on port 7070

### Data Objects:

- GameObject: id: Game_id, col: Column to drop into
```
{
	"id": "f01c8208-e9a1-463e-9912-aa898c90ae65",
	"col": 3
}
```

### APIs for interacting

- POST-  /START/
   - Used for Creating a new Game
   - Return a new game_id
   - The Project works for the Multi Game setup

- GET - /game/{game_id}
  For Fetching game info from game_id
 ```
JSON 
  {
    "success": True,
    "current_state": current_state of game,
    "move_history": move_history
  }
```


- POST - /game/ - For playing on a particular column w.r.t. Game ID
Payload:
```
JSON
{
    "id": <game_id>,
    "col": int(col)
}
```
    

### Improvements:

-   Allowing users to randomly connect and play - Maintaining user ids corresponding to game ids
