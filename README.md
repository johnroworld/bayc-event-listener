# BAYC NFT Transfer Event Listener

## Setup Instructions

1. Clone the repository:
    ```
    git clone https://github.com/johnroworld/KONG-PYTHON.git
    ```
2. Add your Infura API KEY to settings.py:
    ```
    INFURA_API_KEY = 'your_api_key'
    ```
    Note: You can use mine. If there are any permission issues, just reach out to me, and I will grant the necessary permissions.
3. Run migrations:
    ```
    python manage.py migrate
    ```
4. Fetch transfer events:
    ```
    python manage.py fetch_transfer_events
    ```
    Note: Please save one of the token IDs to be used in API usage.
5. Start the Django server:
    ```
    python manage.py runserver
    ```

## API Usage
* Fetch transfer history for a specific BAYC token:
    ```
    GET /api/transfer-history/<token_id>/
    ```
    Note: 
        * Use the saved token ID from instruction #4 in the setup.
        * Use these credentials when consuming GET API: **username: johndoe | password: pass123$



## Future Improvements

1. Only basic authentication only applied to this project. More secure authentication like Token-based authentication must worth a try. A custom Authentication class also needs to be created for reusable authentication.
2. Create unit tests.
3. Use linters like flake8 or pylint for code quality.
4. It is generally not necessary to save logging settings directly in .env file, log-related variables can store (such as log file paths, log levels, etc. This depends on the collaboration of the developers).
