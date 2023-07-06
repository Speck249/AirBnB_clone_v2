#!/usr/bin/env bash
# Install nginx
sudo apt-get update
sudo apt-get install nginx
sudo service nginx start
# Ascertain nginx is running
# sudo service nginx status

# create new directories, if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

# Create fake HTML file
echo "<html>
  <head>
    <title>
    </title>
  </head>
  <body>
        Test Content
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link 
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to user Ubuntu AND group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/^server {/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
