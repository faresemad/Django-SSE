# Django-SSE
Simple Project To Retrieve Data from DB with Django SSE

## Explanation
- Model: The `MyModel` class represents data in the database.
- Serializer: The `MyModelSerializer` class serializes the model data into JSON format.
- View: The `sse_view` function creates an HTTP streaming response that continuously yields JSON-formatted data retrieved from the database. The view uses DRF's `@api_view` decorator to integrate with DRF.
- Client: The HTML page with JavaScript uses the EventSource API to listen for events and update the DOM with the received data.