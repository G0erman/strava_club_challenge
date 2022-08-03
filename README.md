# strava_club_challenge

Automate the data collection and processing to get user activity data from Strava and import it into Google Sheets.

## Configuration Steps - Dev

- Clone repo.
  - Install python libraries gspread, pendulum, typer
- [Configure Strava API account](https://developers.strava.com/docs/getting-started/#account)
  - The user should be an administrator in the Club.  
  - Get Client ID	
  - Get Client Secret
- Configure google Spreadsheet
  - Create a project in [Google Cloud Platform](https://docs.gspread.org/en/latest/oauth2.html#oauth-client-id)
  - Enabled Google Sheets API and Google Drive API
  - Create a service Account
  - Generate new key
  - Ensure you have the right spreadsheet template, for example for
    - Google Key: 12bZWyGzkf81sXCXmiWQNQk-OaanoVIXByz3QbsY7Mpo
    - Share the spreadsheet with the [service account](https://stackoverflow.com/questions/38949318/google-sheets-api-returns-the-caller-does-not-have-permission-when-using-serve)
- Configure the file `.env` with your credentials
  - In mac machines, export the environment vars `export $(cat .env | xargs)`

## Permissions

- Each team member should authorize the App and return the authorization code.
  - Open your Strava account:
  - Return your strava_id
  - Authorize the app (It is necessary to authorize both optional rights: private activities, and strava profile):
    - https://www.strava.com/oauth/authorize?client_id=[YOUR_CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all
  - Return the url generated
  - Execute `python auth_for_strava_user.py strava_id strava_code` to generate the token.

## How to contribute?

- Give me love, welcome any improvement.
- Create new github issue for each contributions. e.g.
  - Create a Dockerfile
  - Add requirement file.
  - Deploy in a cloud environment (Azure, AWS or GCP).
  - Implement CI/CD
  - Call from slack.
  - Improve code quality. PEPs
  - Add features:
    - Cloudword with trips.

## Restrictions

- "gspread.exceptions.APIError: {'code': 429, 'message': "Quota exceeded for quota metric 'Read requests' and limit 'Read requests per minute per user' of service 'sheets.googleapis.com' for consumer 'project_number:592854038195'.", 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.ErrorInfo', 'reason': 'RATE_LIMIT_EXCEEDED', 'domain': 'googleapis.com', 'metadata': {'quota_limit': 'ReadRequestsPerMinutePerUser', 'service': 'sheets.googleapis.com', 'consumer': 'projects/592854038195', 'quota_metric': 'sheets.googleapis.com/read_requests'}}]}"

# Base project:

- https://python.plainenglish.io/how-to-automate-a-club-challenge-with-strava-and-google-sheets-for-dummies-3c9ebc018781

