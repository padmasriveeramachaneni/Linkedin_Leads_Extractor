
import streamlit as st
import requests
from urllib.parse import urlencode
from requests.auth import HTTPBasicAuth
import json
import os

# LinkedIn API credentials (replace with your actual credentials)
CLIENT_ID = '860vvfp9019w9k'       # LinkedIn Client ID from the developer portal
CLIENT_SECRET = 'WPL_AP1.VEj7lMRocajEOKQ7.3kS6yw==' # LinkedIn Client Secret from the developer portal
REDIRECT_URI = 'http://127.0.0.1:3000/callback'
SCOPE = 'r_liteprofile r_emailaddress'

# OAuth 2.0 endpoint to authorize the application
AUTHORIZATION_URL = f"https://www.linkedin.com/oauth/v2/authorization?{urlencode({'response_type': 'code', 'client_id': CLIENT_ID, 'redirect_uri': REDIRECT_URI, 'scope': SCOPE})}"

# Function to get the access token using the authorization code
def get_access_token(authorization_code):
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    
    response = requests.post(token_url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    response_data = response.json()
    
    return response_data.get('access_token')

# Function to fetch profile data from LinkedIn using the access token
def fetch_linkedin_profile_data(access_token):
    profile_url = "https://www.linkedin.com/company/elonnmusk/"
    email_url = "https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))"
    
    headers = {'Authorization': f'Bearer {access_token}'}
    
    # Fetch profile data
    profile_response = requests.get(profile_url, headers=headers)
    profile_data = profile_response.json()
    
    # Fetch email address
    email_response = requests.get(email_url, headers=headers)
    email_data = email_response.json()
    
    # Extract relevant profile information
    profile_info = {
        "name": profile_data.get('localizedFirstName', '') + " " + profile_data.get('localizedLastName', ''),
        "headline": profile_data.get('headline', 'Not available'),
        "location": profile_data.get('location', {}).get('name', 'Not available'),
        "email": email_data['elements'][0]['handle~']['emailAddress'] if 'elements' in email_data else 'Not available'
    }
    
    return profile_info

# Streamlit app for OAuth and displaying LinkedIn profile data
def main():
    st.title("LinkedIn Profile Extractor")
    
    # Step 1: Show a link for the user to authenticate
    st.markdown(f"[Click here to authenticate with LinkedIn]({AUTHORIZATION_URL})")
    
    # Step 2: Collect the authorization code after the user logs in
    authorization_code = st.text_input("Paste the authorization code here")
    
    # Step 3: Get the access token using the authorization code
    if authorization_code:
        access_token = get_access_token(authorization_code)
        if access_token:
            st.success("Successfully authenticated!")
            
            # Step 4: Fetch profile data
            profile_data = fetch_linkedin_profile_data(access_token)
            
            # Step 5: Display the profile data
            st.write("### Profile Data")
            st.write(f"**Name:** {profile_data['name']}")
            st.write(f"**Headline:** {profile_data['headline']}")
            st.write(f"**Location:** {profile_data['location']}")
            st.write(f"**Email:** {profile_data['email']}")
        else:
            st.error("Failed to fetch access token. Please try again.")
    
if __name__ == "__main__":
    main()
