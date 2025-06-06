```mermaid
classDiagram
    %% === Présentation Layer ===
    class PresentationLayer {
        <<Interface>>
        +UserService
        +PlaceService
        +ReviewService
    }

    %% === Business Logic Layer ===
    class BusinessLogicLayer {
        +User
        +Place
        +Review
        +Amenity
        +HBnBFacade
    }

    %% === Persistence Layer ===
    class PersistenceLayer {
        +UserRepository
        +PlaceRepository
        +ReviewRepository
        +AmenityRepository
    }

    %% === Communications ===
    PresentationLayer --> BusinessLogicLayer : uses (via Facade)
    BusinessLogicLayer --> PersistenceLayer : reads/writes data
