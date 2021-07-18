# Fallout Character Generator

## Requirements:
At its core, the project involves creating an application that generates “Objects” upon a set of predefined rules.
The required architecure includes 4 microservices:
1. Controller - takes user input and passes to other services
2. Generator 1 - Generates a thing
3. Generator 2 - Generates another thing
4. Combinor - Generates a third thing based on the output of generator 1 & 2

running update - The system must be able to handle an update, without being shut down. 
This must update must be performed during presentation and so should be noticeable.

## Idea
- Fallout random character creator:
    Creates a random character for fallout 1/2 and updates for Tactics.
    Service 1: Front End allows user to input name/age/gender etc. (do we want to be able to lock somethings in? i.e. choose tags, or allow random)
    Service 2: Generator 1 creates SPECIAL stat array (40 points distributed between 7 stats)
    Service 3: Generator 2 creates a random list of "tag" skills (choose 3 of 18 (tactics still has 18 skills, but they are a different set of 18))
    Service 4: Takes SPECIAL array and tag skills to generate starting stats and derived stats (hp, action points, resistances etc.)

Fallout uses a system of seven primary stats: Strength, Perception, Endurance, Charisma, Intelligence, Agility and Luck. This is called the SPECIAL 
system, due to the acronym of the primary stat names. In addition to these primary stats there are 18 skills which are usd to determine the results 
of in game actions, the default values of these skills are determined by the character's stats. Finally, some additional stats, such as hit points 
and action points are derived from the primary stats, and other features in the game. These are called derived stats.

At character creation a player assigns 40 points between the stats (min 1, max 10) and chooses 3 skills to "tag". Tagged skills start higher and are
easier to improve.

This application will generate a random Fallout character, usable in the games Fallout 1 and 2. An update will also be made to include functionality
for Fallout Tactics, which has a slightly changed list of skills, and a different set of derived stats

### Componets:
- Forms:
    - Service 1: Input basic character details (Name, age, gender)

- Database:
    - Characters - do we store the character?
    - SPECIAL - place to store the stat array
    - Skills - Store the list of skills so we can pull out random ones to tag, also can store the default calculation(?)

- Routes:
    - /, /home: main page, form lives here?
    - /stats: get stat array
    - /skills: get tag skills
    - /construct: calculate skill values and derived stats
    - /output: character sheet (hopefully formatted nicely)

## Actual Product
The flask app has been scaled back so that more project time could be spent on setting up the CI/CD pipeline, no form has been implemented, the randomly generated stats haven't be forced to have a total of 40 and only skill values are calculated. The rolling update is now simply the output being wrapped in a Jinja2 template. There is some implementation of database persistance, however this could not be implemented correctly with the swarm deployment. One potential fix for this would be to deploy a mysql container with the swarm to ensure connectivity, but this would require the database volume to be archived correctly.

The app is unit tested including tests of the content being displayed to the user and testing of the output for services 2,3 and 4. These test that service 2 outputs a list of length 7 as expected, service 3 a list of length 3 and that service 4 correctly calcualtes skills based on set inputs. In the future these tests should check that the stat array sums to 40 and should comprehensively check all skill values are calculated correctly.

## CI/CD Pipeline
The network used for this project consists of three VMs, the Jenkins Controller jenkins-ansible-nginx, the swarm-manager, and the swarm-worker. Originally it was planned that the Jenkins controller would run an nginx load balancer, however this was integrated into the swarm for ease of deployment.

Development and testing is performed on the Jenkins controller, using Git as the VCS. The application is deployed by git-webhook using a Jenkins pipeline. This pipeline has 5 stages: Configure, Build, Test, Push and Deploy. In the Configure stage, the network VMs are configured to use Docker and the swarm is initialised. The Build stage invloves building the images for the Docker containers, and the app is then tested in the Test stage. Finally the images are pushed to dockerhub so they can then be deployed to the swarm.

![Imgur](https://i.imgur.com/bQrocLN.jpg)


## Project Management

As in the first project, a Trello Kanban board was used to track this project's progress:


![Imgur](https://i.imgur.com/Vn4fbph.png)


## Risk Assessment

This project has been risked assessed, with each risk being considered for the effect of the risk, and mitigations that could be implemented to reduce said risk:

![Imgur](https://i.imgur.com/RGM8j6r.png)

## Known Bugs

- Service 4 appears to occasionally return the input rather than the ouptut, could this be some kind of buffer error?

