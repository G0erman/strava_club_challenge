"""
Generate strava token for each team member, it is necessary provide the strava_id and autorization code.

$ python auth_for_strava_user.py strava_team_member_id strava_team_member_code
"""

import json
import os
import requests
import typer


def generate_token(strava_id: int, code: str):
    client_id = int(os.getenv('CLIENT_ID'))
    client_secret = str(os.getenv('CLIENT_SECRET'))

    # Make Strava auth API call with your
    # client_code, client_secret and code
    response = requests.post(
        url='https://www.strava.com/oauth/token',
        data={
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'grant_type': 'authorization_code'
        }
    )

    # Save json response as a variable
    strava_tokens = response.json()
    # Save tokens to file
    with open(f'strava_tokens_{strava_id}.json', 'w') as outfile:
        json.dump(strava_tokens, outfile)

    print(outfile)

    # Open JSON file and print the file contents
    # to check it's worked properly
    with open(f'strava_tokens_{strava_id}.json') as check:
        data = json.load(check)

    print(data)


if __name__ == "__main__":
    typer.run(generate_token)