```mermaid
classDiagram
    class User {
        +UUID id
        +str first_name
        +str last_name
        +str email
        +str password
        +bool is_admin
        +datetime created_at
        +datetime updated_at
        +register()
        +update_profile()
        +delete()
    }

    class Place {
        +UUID id
        +str title
        +str description
        +float price
        +float latitude
        +float longitude
        +UUID owner_id
        +datetime created_at
        +datetime updated_at
        +create()
        +update()
        +delete()
    }

    class Review {
        +UUID id
        +int rating
        +str comment
        +UUID user_id
        +UUID place_id
        +datetime created_at
        +datetime updated_at
        +create()
        +update()
        +delete()
    }

    class Amenity {
        +UUID id
        +str name
        +str description
        +datetime created_at
        +datetime updated_at
        +create()
        +update()
        +delete()
    }

    %% Relations
    User "1" --> "0..*" Place : owns >
    Place "1" --> "0..*" Review : receives >
    User "1" --> "0..*" Review : writes >
    Place "1" o-- "*" Amenity : has >
