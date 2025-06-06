```mermaid
classDiagram
    class User {
        -id : UUID
        +first_name : str
        +last_name : str
        +email : str
        -password : str
        -is_admin : bool
        +created_at : datetime
        +updated_at : datetime
        +register()
        -update_profile()
        -delete()
        +write_review()
    }

    class Place {
        -id : UUID
        +title : str
        +description : str
        +price : float
        +latitude : float
        +longitude : float
        -owner_id : UUID
        +created_at : datetimne
        +updated_at : datetime
        +create()
        -update()
        -delete()
        +get_owner()
        +add_amenity()
        +remove_amenity()
    }

    class Review {
        -id : UUID
        +rating : int
        +comment : str
        -user_id : UUID
        -place_id : UUID
        +created_at : datetime
        +updated_at : datetime
        +create()
        -update()
        -delete()
        +get_user()
        +get_place()
    }

    class Amenity {
        -id : UUID
        +name : str
        +description : str
        +created_at : datetime
        +updated_at : datetime
        +create()
        -update()
        -delete()
    }

    %% Relations
    User "1" --> "0..*" Place : owns >
    Place "1" --> "0..*" Review : receives >
    User "1" --> "0..*" Review : writes >
    Place "1" o-- "*" Amenity : has >
