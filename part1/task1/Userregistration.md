sequenceDiagram
participant User
participant API
participant BusinessLogic
participant DB

User->>API: Send email, password, name
API->>BusinessLogic: Validate input data

alt Missing fields
    BusinessLogic-->>API: Error "field required"
    API-->>User: 400 Bad Request
else Email already used
    BusinessLogic->>DB: Check if email exists
    DB-->>BusinessLogic: Email found
    BusinessLogic-->>API: Error "email already used"
    API-->>User: 409 Conflict
else Valid input
    BusinessLogic->>BusinessLogic: Hash password
    BusinessLogic->>DB: Save new user
    DB-->>BusinessLogic: Save OK
    BusinessLogic-->>API: Return new user
    API-->>User: 201 Created
end
