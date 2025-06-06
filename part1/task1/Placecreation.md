sequenceDiagram
participant Client
participant API
participant PlaceService
participant Storage

Client->>API: POST /places (title, description, price, etc.)
API->>PlaceService: process_new_place(data)

alt All required fields are valid
    PlaceService->>Storage: insert_place(data)
    Storage-->>PlaceService: return place_id
    PlaceService-->>API: return created place
    API-->>Client: 201 Created { "id": place_id, ... }
else Validation error
    PlaceService->>PlaceService: check required fields
    PlaceService-->>API: return "Missing required fields"
    API-->>Client: 422 Unprocessable Entity { "error": "Missing title" }
else Database error
    PlaceService->>Storage: insert_place(data)
    Storage-->>PlaceService: error (DB down)
    PlaceService-->>API: return database error
    API-->>Client: 503 Service Unavailable { "error": "Database issue" }
end
