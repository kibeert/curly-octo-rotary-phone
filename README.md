﻿# curly-octo-rotary-phone
# Event Countdown Timer

This project is a simple web application built with Django that displays countdown timers for various events. Users can add, edit, and delete events, and the countdown timers will update accordingly.

## Features

- Display countdown timers for multiple events.
- Add new events with specified names and dates.
- Edit existing events to update their names or dates.
- Delete events when they are no longer needed.

## Installation

1. Clone this repository to your local machine:

    ```
    git clone <https://github.com/kibeert/curly-octo-rotary-phone/edit/main/README.md>
    ```

2. Navigate to the project directory:

    ```
    cd event-countdown-timer
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```
    python manage.py migrate
    ```

5. Run the development server:

    ```
    python manage.py runserver
    ```

6. Access the application in your web browser at `http://localhost:8000/`.

## Usage

1. **View Countdown Timers:**
   - Upon accessing the application, you will see countdown timers for all existing events.
   - Each timer displays the name of the event and the time remaining until its scheduled date.

2. **Add New Event:**
   - Click the "Add Event" button to create a new event.
   - Enter the name and date for the event in the form provided.
   - Click "Save" to add the event.

3. **Edit Existing Event:**
   - Click the "Edit" button on the event timer you wish to edit.
   - Modify the name or date of the event in the form provided.
   - Click "Save" to update the event.

4. **Delete Event:**
   - Click the "Delete" button on the event timer you wish to delete.
   - Confirm the deletion when prompted.

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
