# Update script for clab

sudo clab version upgrade
# Set SUID bit on Containerlab binary
sudo chmod u+s `which containerlab`
# Create clab_admins Unix group
sudo groupadd -r clab_admins
# Add current user to clab_admins group
sudo usermod -aG clab_admins admin