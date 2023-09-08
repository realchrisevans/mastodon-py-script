import requests
from bs4 import BeautifulSoup
from mastodon import Mastodon

# Set up your Mastodon API credentials
mastodon_instance_url = "https://mastodon.social"
mastodon_token = "YOUR_MASTODON_ACCESS_TOKEN"  # You need to generate this token

# URL of your Hashnode blog
hashnode_blog_url = "https://hashnode.com/@realchrisevans"

# Initialize the Mastodon API client
mastodon = Mastodon(
    access_token=mastodon_token,
    api_base_url=mastodon_instance_url,
)

# Function to check for new blog posts and post to Mastodon
def check_and_post_new_blog():
    # Send a GET request to your Hashnode blog page
    response = requests.get(hashnode_blog_url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Check for the latest blog post title (assuming it's in an <h1> element)
        latest_blog_title = soup.find("h1").text

        # You can add more logic here to check if this is a new post
        # For simplicity, we assume any post is new

        # Compose the Mastodon message
        mastodon_message = f"📝 New blog post: '{latest_blog_title}' {hashnode_blog_url}"

        # Post the message to Mastodon
        mastodon.status_post(mastodon_message)

        print("Posted to Mastodon:", mastodon_message)
    else:
        print("Error accessing Hashnode blog.")

# Run the function to check for and post new blog posts
check_and_post_new_blog()
import requests
from bs4 import BeautifulSoup
from mastodon import Mastodon

# Set up your Mastodon API credentials
mastodon_instance_url = "https://mastodon.social"
mastodon_token = "56DeMrKbg-j31ko3ZJ8EKUTdHy4iIx1SIr1dMWgB2KgS"  # You need to generate this token

# URL of your Hashnode blog
hashnode_blog_url = "https://hashnode.com/@realchrisevans"

# Initialize the Mastodon API client
mastodon = Mastodon(
    access_token=mastodon_token,
    api_base_url=mastodon_instance_url,
)

# Function to check for new blog posts and post to Mastodon
def check_and_post_new_blog():
    # Send a GET request to your Hashnode blog page
    response = requests.get(hashnode_blog_url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Check for the latest blog post title (assuming it's in an <h1> element)
        latest_blog_title = soup.find("h1").text

        # You can add more logic here to check if this is a new post
        # For simplicity, assume any post is new

        # Compose the Mastodon message
        mastodon_message = f"📝 New blog post: '{latest_blog_title}' {hashnode_blog_url}"

        # Post the message to Mastodon
        mastodon.status_post(mastodon_message)

        print("Posted to Mastodon:", mastodon_message)
    else:
        print("Error accessing Hashnode blog.")

# Run the function to check for and post new blog posts
check_and_post_new_blog()
