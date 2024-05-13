#!/usr/bin/env bash

# Import the Datadog repository key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C7A7DA52AB3C4F70

# Add the Datadog repository
echo "deb https://apt.datadoghq.com/ stable 7" | sudo tee /etc/apt/sources.list.d/datadog.list

# Update the package list
sudo apt-get update

# Install the Datadog agent
sudo apt-get install datadog-agent -y

# Check if installation was successful
if [ $? -eq 0 ]; then
    # Configure the Datadog agent
    sudo sed -i "s/# logs_enabled:.*/logs_enabled: true/" /etc/datadog-agent/datadog.yaml
    sudo sed -i "s/# logs_config:.*/logs_config:/" /etc/datadog-agent/datadog.yaml
    sudo sed -i "s/#   - type:.*/  - type: file/" /etc/datadog-agent/datadog.yaml
    sudo sed -i "s|#     path:.*|    path: /var/log/nginx/access.log|" /etc/datadog-agent/datadog.yaml
    sudo sed -i "s/#     service:.*/    service: nginx/" /etc/datadog-agent/datadog.yaml

    # Restart the Datadog agent
    sudo service datadog-agent restart
else
    echo "Datadog agent installation failed."
fi

