# BAYC NFT Transfer Event Listener
## Django application that connects to the Ethereum blockchain via Infura to listen for and record transfer events of Bored Ape Yacht Club (BAYC) NFTs.

## Setup Instructions

1. Clone the repository:
    ```
    git clone https://github.com/johnroworld/bayc-event-listener.git
    ```
    
2. Add your Infura API KEY to settings.py:
    ```
    INFURA_API_KEY = 'your_api_key'
    ```
    **Note: You can use the one in the settings. If there are any permission issues, just reach out to me, and I will grant the necessary permissions.**
   
4. Run migrations:
    ```
    python manage.py migrate
    ```
    
5. Fetch transfer events:
    ```
    python manage.py fetch_transfer_events
    ```
    **Note: Please save one of the token IDs from the results for API usage.**
   
7. Start the Django server:
    ```
    python manage.py runserver
    ```

## API Usage
* Fetch transfer history for a specific BAYC token:
    ```
    GET /api/transfer-history/<token_id>/
    ```
    **Note: 
        * Use the saved token ID from instruction #4 in the setup.
        * Enter the following credentials when consuming the GET API: Username: johndoe | Password: pass123$**


## Future Improvements

1. Only basic authentication only applied to this project. More secure authentication like Token-based authentication must worth a try. A custom Authentication class also needs to be created for reusable authentication.
2. Create unit tests.
3. Use linters like flake8 or pylint for code quality.
4. It is generally not necessary to save logging settings directly in .env file, log-related variables can store (such as log file paths, log levels, etc. This depends on the collaboration of the developers).
