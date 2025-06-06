# HBNB
## Introduction
HBNB is a minimalist Airbnb-like platform that allows users to list and explore rental properties. Currently, it does not include a payment system or booking functionality, but it will provide a solid foundation for managing places, users, and related data.
Project is still under development, but feel free to take a look at our files !
## 2. Project Directory Structure
```
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```
## 3. Explanation of Directories and Files
The directory contains the core application code.app/
The subdirectory houses the API endpoints, organized by version ().api/v1/
The subdirectory contains the business logic classes (e.g., , ).models/user.pyplace.py
The subdirectory is where the Facade pattern is implemented, managing the interaction between layers.services/
The subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.persistence/
run.py is the entry point for running the Flask application.
config.py will be used for configuring environment variables and application settings.
requirements.txt will list all the Python packages needed for the project.
README.md will contain a brief overview of the project.
The in-memory repository will handle object storage and validation. It follows a consistent interface that will later be replaced by a database-backed repository.

## 4. The Facade Pattern in HBNB
The Facade pattern is a structural design pattern that provides a simplified interface to a complex system, making it easier for clients to interact with it. In the context of the HBnB project, the Facade pattern plays a crucial role in managing the interactions between the Presentation layer (API) and the Business Logic layer, while also serving as an intermediary that will later connect to the Persistence layer. This article will explore how the Facade pattern is implemented in this part of the project and how it streamlines the overall system architecture.
Describe the purpose of each directory and file.
Include instructions on how to install dependencies and run the application.

## 5.Implementation of the In-Memory Repository
Inside repository.py, the in-memory repository and interface will be fully implemented:

## 6. Creating the HBnBFacade Class
In the subdirectory, create a file where you will define the class. This class will handle communication between the Presentation, Business Logic, and Persistence layers. You  will interact with the repositories (like the in-memory repository) through this Class:services/facade.pyHBnBFacade
The methods in the Facade use placeholders to avoid errors during initial testing. The actual logic will be added in future tasks.
In the root directory, create the file that will serve as the entry point for running the application:run.py
In the file, list the Python packages needed for the project:requirements.txt

## 7. Running the Application
Install Dependencies
Ensure you have Python installed, then run:
```
pip install -r requirements.txt
```
Start the Flask Application
To run the application, execute:
```
python run.py
```