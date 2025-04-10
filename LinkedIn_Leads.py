
import streamlit as st
import requests
from PIL import Image  # Import for handling images
from streamlit_option_menu import option_menu  # Import for option menu

# Page icon
icon = Image.open("D:/All Documents/Projects/LinkedIn/Logo.png")

# Page configuration
st.set_page_config(
    page_title="LinkedIn Leads Finder",
    page_icon=icon,
    layout="wide",
    initial_sidebar_state="expanded",
)

# Developer credit
st.markdown("<h2 style='text-align: center; color: #000080;'>LinkedIn Profile Leads Fetcher</h2>", unsafe_allow_html=True)
st.text("")
st.text("")

# Background Styling
background_image_path = "D:/All Documents/Projects/LinkedIn/Logo.png"
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('{background_image_path}');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.balloons()

# Sidebar menu
with st.sidebar:
    st.sidebar.image(icon, use_column_width=True)
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Project Details", "Contact"],
        menu_icon="cast", 
        default_index=0,
    )

# Home Section
if selected == "Home":

    # Set up the Proxycurl API endpoint and API key
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    api_key = '-iwApnQnf7RhrBG-PTUiiA'  

    # Set up headers for the API request
    headers = {'Authorization': 'Bearer ' + api_key}

    # Input for the LinkedIn profile URL
    linkedin_profile_url = st.text_input("Enter the LinkedIn Profile URL:")

    # Fetch data when the button is clicked
    if st.button("Fetch Profile Data"):
        if linkedin_profile_url:
            # Set up parameters for the API request
            params = {'url': linkedin_profile_url, 'skills': 'include', 'extra': 'include'}

            # Send request to Proxycurl API
            response = requests.get(api_endpoint, params=params, headers=headers)

            # Check for successful response
            if response.status_code == 200:
                profile_data = response.json()

                # Display each field with st.markdown and color styling
                st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Profile Picture URL:</span> <span style='color:#333'>{profile_data.get('profile_pic_url', 'Data Not Found')}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='color:#0073e6; font-weight:bold'>First Name:</span> <span style='color:#333'>{profile_data.get('first_name', 'Data Not Found')}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Last Name:</span> <span style='color:#333'>{profile_data.get('last_name', 'Data Not Found')}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Full Name:</span> <span style='color:#333'>{profile_data.get('full_name', 'Data Not Found')}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Occupation:</span> <span style='color:#333'>{profile_data.get('occupation', 'Data Not Found')}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Headline:</span> <span style='color:#333'>{profile_data.get('headline', 'Data Not Found')}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Summary:</span> <span style='color:#333'>{profile_data.get('summary', 'Data Not Found')}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Industry:</span> <span style='color:#333'>{profile_data.get('industry', 'Data Not Found')}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Personal Emails:</span> <span style='color:#333'>{profile_data.get('personal_emails', 'Data Not Found')}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Personal Numbers:</span> <span style='color:#333'>{profile_data.get('personal_numbers', 'Data Not Found')}</span>", unsafe_allow_html=True)

                # Display Education information
                st.write("### Education")
                education = profile_data.get('education', [])
                if education:
                    for edu in education:
                        st.markdown(f"<span style='color:#0073e6; font-weight:bold'>School:</span> <span style='color:#333'>{edu.get('school', 'Data Not Found')}</span>", unsafe_allow_html=True)
                        st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Degree:</span> <span style='color:#333'>{edu.get('degree_name', 'Data Not Found')}</span>", unsafe_allow_html=True)
                        st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Field of Study:</span> <span style='color:#333'>{edu.get('field_of_study', 'Data Not Found')}</span>", unsafe_allow_html=True)

                        # Safely access duration (start_date and end_date)
                        start_date = edu.get('starts_at', {})
                        end_date = edu.get('ends_at', {})

                        # Handle missing start_date or end_date
                        start_day = start_date.get('day', 'Data Not Found') if start_date else 'Data Not Found'
                        start_month = start_date.get('month', 'Data Not Found') if start_date else 'Data Not Found'
                        start_year = start_date.get('year', 'Data Not Found') if start_date else 'Data Not Found'

                        end_day = end_date.get('day', 'Data Not Found') if end_date else 'Data Not Found'
                        end_month = end_date.get('month', 'Data Not Found') if end_date else 'Data Not Found'
                        end_year = end_date.get('year', 'Data Not Found') if end_date else 'Data Not Found'

                        # Format the duration in DD-MM-YYYY
                        start_date_str = f"{start_day}-{start_month}-{start_year}"
                        end_date_str = f"{end_day}-{end_month}-{end_year}"

                        # Display the formatted date range
                        st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Duration:</span> <span style='color:#333'>{start_date_str} - {end_date_str}</span>", unsafe_allow_html=True)

                        st.markdown("---")
                else:
                    st.write("Data Not Found")

                # Display Skills as a comma-separated list
                st.write("### Skills")
                if 'skills' in profile_data:
                    skills = profile_data['skills']
                    if skills:
                        skill_list = ', '.join(skills)  # Join the skills into a comma-separated string
                        st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Skills:</span> <span style='color:#333'>{skill_list}</span>", unsafe_allow_html=True)
                    else:
                        st.write("Data Not Found")
                else:
                    st.write("Data Not Found")

                # Display Experience information
                st.write("### Experience")
                experiences = profile_data.get('experiences', [])
                if experiences:
                    for experience in experiences:
                        st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Company:</span> <span style='color:#333'>{experience.get('company', 'Data Not Found')}</span>", unsafe_allow_html=True)
                        st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Title:</span> <span style='color:#333'>{experience.get('title', 'Data Not Found')}</span>", unsafe_allow_html=True)
                        st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Description:</span> <span style='color:#333'>{experience.get('description', 'Data Not Found')}</span>", unsafe_allow_html=True)
                        st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Location:</span> <span style='color:#333'>{experience.get('location', 'Data Not Found')}</span>", unsafe_allow_html=True)

                        # Safely access duration
                        start_date = experience.get('starts_at', {})
                        end_date = experience.get('ends_at', {})

                        # Handle missing start_date or end_date
                        start_day = start_date.get('day', 'Data Not Found') if start_date else 'Data Not Found'
                        start_month = start_date.get('month', 'Data Not Found') if start_date else 'Data Not Found'
                        start_year = start_date.get('year', 'Data Not Found') if start_date else 'Data Not Found'

                        end_day = end_date.get('day', 'Data Not Found') if end_date else 'Data Not Found'
                        end_month = end_date.get('month', 'Data Not Found') if end_date else 'Data Not Found'
                        end_year = end_date.get('year', 'Data Not Found') if end_date else 'Data Not Found'

                        # Format the duration in DD-MM-YYYY
                        start_date_str = f"{start_day}-{start_month}-{start_year}"
                        end_date_str = f"{end_day}-{end_month}-{end_year}"

                        # Display the formatted date range
                        st.markdown(f"<span style='color:#0073e6; font-weight:bold'>Duration:</span> <span style='color:#333'>{start_date_str} - {end_date_str}</span>", unsafe_allow_html=True)
                        
                        st.markdown("---")
                else:
                    st.write("Data Not Found")

            else:
                st.error("Error fetching data. Please check the LinkedIn profile URL.")
        else:
            st.warning("Please enter a LinkedIn profile URL.")


            
elif selected == "Project Details":
     # Header
    st.markdown("<h2 class='sider-title' style='color: SlateGray ;'>Project Details</h2>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.markdown("<h3 class= 'sider-title' style='color: black;'>About This Fetcher:</h3>",unsafe_allow_html=True)
    st.write("")
    st.write("The LinkedIn Leads Finder is a Streamlit-based app that fetches LinkedIn profile data using the Proxycurl API. Users input a LinkedIn profile URL, and the app retrieves details like name, occupation, contact information, education, skills, and work experience.")
    st.write("")
    st.write("The data is displayed in a well-organized, color-coded layout for easy readability. Each section of the profile, such as skills or work experience, is clearly separated for better user experience. This tool is designed to simplify the process of lead generation or researching LinkedIn profiles, providing quick access to detailed and structured profile information.")
    st.write("")
    image="D:/All Documents/Projects/LinkedIn/Logo.png"
    image = Image.open(image)
    st.image(image, caption="Leads Extractor Logo", width=500, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
    
elif selected == "Contact":
    # Header
    st.markdown("<h2 class='sider-title' style='color: SlateGray;'>Developer Details</h2>", unsafe_allow_html=True)
    st.text("")
    
    # Load and resize image for the team member
    nithin = Image.open("D:/All Documents/Projects/LinkedIn/Nithin.JPG").resize((900, 900))

    # Display the team member's image and details
    st.image(nithin, caption="Nithin Reddy Cheerapureddy", use_column_width=True)
    st.write("Name: Nithin Reddy Ch")
    st.write("Phone: +91 6302810409")
    st.write("Email: nithin9231@gmail.com")
