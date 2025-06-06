```mermaid
sequenceDiagram
    participant User
    participant API
    participant Review Service
    participant Review

    %% Soumission d'une nouvelle review
    User ->> API: POST /reviews (rating, comment, place_id)
    API ->> Review Service: create Review(rating, comment, place_id, user_id)

    alt Valid Data
        Review Service ->> Review: new Review(rating, comment, place_id, user_id)
        Review ->> Review: create()
        Note right of Review: Génère UUID, created_at, updated_at<br/>Valide les champs
        Review -->> Review Service: Review instance
        Review Service -->> API: Return success (201 Created)
        API -->> User: 201 Created (Review enregistrée)
    else Invalid Data
        Review Service -->> API: Return error (400 Bad Request)
        API -->> User: 400 Bad Request (Invalid review data)
    else Unexpected Error
        Review Service -->> API: Return HTTP 500
        API -->> User: 500 Internal Server Error
    end

    %% Récupération d'une review existante
    User ->> API: GET /reviews/{review_id}
    API ->> Review Service: get Review By Id(review_id)
    Review Service ->> Review: fetch By Id(review_id)
    Review -->> Review Service: Review data

    alt Review Found
        Review Service -->> API: send Review data
        API -->> User: 200 OK (Review details)
    else Review Not Found
        Review -->> Review Service: null
        Review Service -->> API: 404 Not Found
        API -->> User: 404 Not Found (Review does not exist)
    end
