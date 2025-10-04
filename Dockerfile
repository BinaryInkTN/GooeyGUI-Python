FROM ubuntu:22.04

WORKDIR /app

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install system dependencies including git and SSH client
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    python3-tk \
    git \
    && rm -rf /var/lib/apt/lists/*


# Clone the repository (using HTTPS to avoid SSH key issues in Docker)
RUN git clone https://github.com/BinaryInkTN/GooeyGUI-Installer.git

WORKDIR /app/GooeyGUI-Installer

# Add any additional commands you want to run after cloning
# For example:
# RUN ls -la
# RUN python setup.py install

# Keep the container running or set appropriate CMD
CMD ["/bin/bash"]
