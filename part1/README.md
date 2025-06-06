# HBNB – API Design & System Architecture

## 🧾 Introduction

This document presents the system design and internal structure of the **HBNB web application**, following a layered architecture approach.

The main goal of this documentation is to:
- Clearly illustrate how the system is organized across layers (Presentation, Business Logic, and Persistence)
- Detail the data models and their relationships
- Explain how key API endpoints behave using sequence diagrams

All diagrams are written using **Mermaid.js** and aim to help developers quickly understand the backend structure, interaction flow, and responsibility of each component.

---

## 🧱 1. Architecture Overview

This first diagram shows the **three main layers** of the application:

- **Presentation Layer**: Responsible for handling user/API requests.
- **Business Logic Layer**: Processes data, applies rules, and handles core operations.
- **Persistence Layer**: Manages the storage and retrieval of data from the database.

```mermaid
<!-- architecture_layers.md -->
classDiagram
    class PresentationLayer {
        <<Interface>>
        +UserService
        +PlaceService
        +ReviewService
    }

    class BusinessLogicLayer {
        +User
        +Place
        +Review
        +Amenity
        +HBnBFacade
    }

    class PersistenceLayer {
        +UserRepository
        +PlaceRepository
        +ReviewRepository
        +AmenityRepository
    }

    PresentationLayer --> BusinessLogicLayer : uses (via Facade)
    BusinessLogicLayer --> PersistenceLayer : reads/writes data
