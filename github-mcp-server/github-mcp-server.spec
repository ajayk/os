%global debug_package %{nil}

Name:           github-mcp-server
Version:        0.1.0
Release:        1%{?dist}
Summary:        GitHub MCP (Model Context Protocol) Server
License:        MIT
URL:            https://github.com/github/github-mcp-server
Source0:        https://github.com/github/github-mcp-server/archive/refs/heads/main.tar.gz

BuildRequires:  golang >= 1.21
BuildRequires:  git
Requires:       docker-ce >= 20.10.0

%description
The GitHub MCP Server is a Model Context Protocol (MCP) server that provides
seamless integration with GitHub APIs, enabling advanced automation and
interaction capabilities for developers and tools.

%prep
%autosetup -n %{name}-main

%build
cd cmd/github-mcp-server
go build -o github-mcp-server

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 cmd/github-mcp-server/github-mcp-server %{buildroot}%{_bindir}/github-mcp-server

# Install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
install -p -m 644 README.md %{buildroot}%{_docdir}/%{name}/
install -p -m 644 LICENSE %{buildroot}%{_docdir}/%{name}/

# Install systemd service file
mkdir -p %{buildroot}%{_unitdir}
cat > %{buildroot}%{_unitdir}/github-mcp-server.service << EOF
[Unit]
Description=GitHub MCP Server
After=network.target

[Service]
Type=simple
ExecStart=%{_bindir}/github-mcp-server stdio
Restart=on-failure
Environment=GITHUB_PERSONAL_ACCESS_TOKEN=

[Install]
WantedBy=multi-user.target
EOF

# Create configuration directory
mkdir -p %{buildroot}%{_sysconfdir}/github-mcp-server
cat > %{buildroot}%{_sysconfdir}/github-mcp-server/config.json.example << EOF
{
  "TOOL_ADD_ISSUE_COMMENT_DESCRIPTION": "Add a comment to an existing issue",
  "TOOL_CREATE_BRANCH_DESCRIPTION": "Create a new branch in a GitHub repository"
}
EOF

%files
%license LICENSE
%doc README.md
%{_bindir}/github-mcp-server
%{_unitdir}/github-mcp-server.service
%dir %{_sysconfdir}/github-mcp-server
%config(noreplace) %{_sysconfdir}/github-mcp-server/config.json.example

%post
%systemd_post github-mcp-server.service

%preun
%systemd_preun github-mcp-server.service

%postun
%systemd_postun_with_restart github-mcp-server.service

%changelog
* Mon Apr 07 2025 AjayK <maintainer@example.com> - 0.1.0-1
- Initial package
