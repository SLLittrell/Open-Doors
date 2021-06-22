
# Open Doors

## Motive

1. Utilize and expand knowledge of REACT and Django Rest Framework
1. Create an application using CRUD functionality
1. Produce a easy to use application for families, teachers, and caregivers


## What is Open Doors?

 An application to help families, educators, or caregivers explore local events and attractions alongside neurodiverse children with confidence. Also to create resources for children who may experience challenges with social communication using methods such as Social Stories. 

### Installation
Clone Open-Doors-Server repository (https://github.com/SLLittrell/Open-Doors-Server)
Clone Open-Doors-Client repository (https://github.com/SLLittrell/Open-Doors-Client)

## Client
Run
```
npm install

npm start 
```
## Server
-[ ] Run virtual environment
-[ ] Run migrations
```
python3 manage.py loaddata categories posts tokens users open_user stories
```

```
python3 manage.py runserver
```

login using fixture data

### Features
- login/registration 
- Post, Story, and Schedules features are CRUD ready
- Users can Search attraction by city name.
- User can create a social story from attraction details or from social story info page.
- User can create a Visual schedule by navigating to the affordance on the schedule info page.
- User can create a post to the community board, and view all approved posts
- User can add Social Stories and Visual schedules to posts
- On navigating to My Library the user has access to their created stories and schedules, with the ability to View 
- Two user types-Authenticated user, and Admin user
- Admin users have access to approve posts before all users can view it. 


### ERD
![Open Doors ERD (1)]()

### Wireframe
![Open Doors WireFrame]()

### Support
Fill out a support ticket if you discover any major bugs to address. 


### Roadmap
Planned features include: 

- Search attraction type
- integrated images search for stories and schedules 
- More comprehensive styling
- More Admin user features

### Contributing
Feel free to fork the repository and make pull requests. That said, we have no plans to maintain this project. 

### Authors & Acknowledgments
Special thanks to our team mentor [Scott Silver](https://github.com/Scott47) for his support and advice on this project.  

[Stacey Littrell](https://github.com/SLLittrell)

## A Note About Authentication

The login and registration code we use is fake, completely insecure, and would never be implemented in a professional application. It is a simulation authentication using very simplistic tools, because authentication is not a learning objective of students at NSS.
