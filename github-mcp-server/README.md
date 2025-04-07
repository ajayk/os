# GitHub MCP Server Package

This package contains the necessary files to build and install the [GitHub MCP Server](https://github.com/github/github-mcp-server), which is a Model Context Protocol (MCP) server that provides seamless integration with GitHub APIs.

## Features

- Integrate with GitHub APIs through the Model Context Protocol
- Automate GitHub workflows and processes
- Extract and analyze data from GitHub repositories
- Build AI-powered tools that interact with GitHub's ecosystem

## Installation Methods

### Arch Linux (PKGBUILD)

```bash
# Clone this repository
git clone https://github.com/ajayk/os.git
cd os/github-mcp-server

# Build and install the package
makepkg -si
```

### Fedora/RHEL/CentOS (RPM)

```bash
# Clone this repository
git clone https://github.com/ajayk/os.git
cd os/github-mcp-server

# Build the RPM package
rpmbuild -bb github-mcp-server.spec

# Install the RPM
sudo dnf install ~/rpmbuild/RPMS/x86_64/github-mcp-server-0.1.0-1*.rpm
```

### Debian/Ubuntu (DEB)

```bash
# Clone this repository
git clone https://github.com/ajayk/os.git
cd os/github-mcp-server

# Build the Debian package
dpkg-buildpackage -us -uc -b

# Install the package
sudo dpkg -i ../github-mcp-server_0.1.0-1_amd64.deb
sudo apt-get install -f  # Install any missing dependencies
```

### Docker

```bash
# Clone this repository
git clone https://github.com/ajayk/os.git
cd os/github-mcp-server

# Build the Docker image
docker build -t github-mcp-server .

# Run the container
docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN="your_token_here" github-mcp-server
```

## Configuration

After installation, you'll need to configure your GitHub Personal Access Token:

1. [Create a GitHub Personal Access Token](https://github.com/settings/personal-access-tokens/new)
2. Set the token as an environment variable:
   ```bash
   export GITHUB_PERSONAL_ACCESS_TOKEN="your_token_here"
   ```

### Using with VS Code

Add the following to your VS Code settings.json file:

```json
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "github_token",
        "description": "GitHub Personal Access Token",
        "password": true
      }
    ],
    "servers": {
      "github": {
        "command": "github-mcp-server",
        "args": ["stdio"],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github_token}"
        }
      }
    }
  }
}
```

## License

This package is under the same license as the original GitHub MCP Server (MIT).
