## News Highlight
News Highlight is an application that gives a user an easy time locating the kind of news they want to follow

## Author
Juliet Koech

## Date made
23/6/2019

## Technologies Used
1. Python3.7
2. Html
3. Bootstrap
4. Python Extensions
5. Flask

## Using the application
* You require a minimum python version 3.6 to run the application 
* Clone the repository and get to install flask using git clone  https://github.com/Julzpeter/News-highlight
* Run the application
* Click on the link on the terminal as you press ctrl and use the application in the browser

# creating a virtual environment
* python3.7 -m venv --without-pip virtual
* source virtual/bin/activate

# installing dependacies
pip install -r requirements

# running test
python3.7 manage.py test

# running the development
* python run.py
* open the app on your browser 127.0.0.1:5000.
* Deploying to heroku make sure you have requirements.txt

## Behavior Driven Development


|Behavior                                       | Input                  | Output                                   |
|-----------------------------------------------|------------------------|------------------------------------------| 
| Dsiplay all articles based on a single source | ABC on input form      | Display all articles for ABC             |
| Read an article on its url page               | Click Read more button | Redirect to respective articles homepage |