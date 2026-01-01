#!/usr/bin/env python3
"""
Portainer to Dockge Template Converter

Converts Portainer JSON templates to Dockge-compatible Docker Compose format.
Supports batch conversion, single file output, and interactive mode.

Author: Snaplyze
License: MIT
"""

import json
import os
import sys
import argparse
import re
import urllib.request
import urllib.error
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional


class PortainerToDockgeConverter:
    """Converts Portainer templates to Dockge Docker Compose format."""
    
    # Default path mappings from Portainer to Dockge
    DEFAULT_PATH_MAPPINGS = {
        "/portainer/Files/AppData/Config/": "/opt/stacks/{service_name}/data/",
        "/var/lib/": "/opt/stacks/{service_name}/data/lib/",
    }
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize converter with optional configuration.
        
        Args:
            config: Configuration dictionary with custom settings
        """
        self.config = config or {}
        self.base_path = self.config.get('base_path', '/opt/stacks')
        self.create_readme = self.config.get('create_readme', True)
        self.create_env = self.config.get('create_env', True)
        self.skip_types = self.config.get('skip_types', [])
        self.custom_mappings = self.config.get('custom_mappings', {})
        self.download_timeout = self.config.get('download_timeout', 10)
        
    def parse_portainer_templates(self, json_file: str) -> List[Dict[str, Any]]:
        """
        Parse Portainer templates JSON file.
        
        Args:
            json_file: Path to portainer-templates.json
            
        Returns:
            List of template dictionaries
        """
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('templates', [])
        except Exception as e:
            print(f"Error reading {json_file}: {e}")
            sys.exit(1)
    
    def convert_ports(self, portainer_ports: List[str]) -> List[str]:
        """
        Convert Portainer port format to Docker Compose format.
        
        Examples:
            :80/tcp -> "80:80"
            8080:80/tcp -> "8080:80"
            3306/tcp -> "3306:3306"
            5432 -> "5432:5432"
        
        Args:
            portainer_ports: List of Portainer port strings
            
        Returns:
            List of Docker Compose formatted port strings
        """
        result = []
        for port in portainer_ports:
            # Remove protocol suffix (/tcp, /udp)
            port_clean = re.sub(r'/(tcp|udp)$', '', port)
            
            if port_clean.startswith(':'):
                # Auto-mapping: :80 -> 80:80
                container_port = port_clean[1:]
                result.append(f'"{container_port}:{container_port}"')
            elif ':' in port_clean:
                # Explicit mapping: 8080:80 -> "8080:80"
                result.append(f'"{port_clean}"')
            else:
                # Only container port: 80 -> "80:80"
                result.append(f'"{port_clean}:{port_clean}"')
        
        return result
    
    def map_volume_path(self, bind_path: Optional[str], container_path: str, 
                       service_name: str) -> str:
        """
        Intelligently map volume paths from Portainer to Dockge format.
        
        Args:
            bind_path: Host bind path from Portainer (can be None)
            container_path: Container path
            service_name: Name of the service
            
        Returns:
            Mapped host path for Dockge
        """
        # Check for custom mappings first
        if service_name in self.custom_mappings:
            custom = self.custom_mappings[service_name]
            if container_path in custom:
                return custom[container_path]
        
        # If no bind path specified, create one based on container path
        if not bind_path:
            # Clean container path for use in host path
            subpath = container_path.strip('/').replace('/', '_')
            if subpath:
                return f'{self.base_path}/{service_name}/data/{subpath}'
            else:
                return f'{self.base_path}/{service_name}/data'
        
        # Map Portainer paths to Dockge paths
        if bind_path.startswith('/portainer/Files/AppData/Config/'):
            # Determine purpose based on container path
            if container_path in ['/config', '/data']:
                return f'{self.base_path}/{service_name}/data'
            elif container_path.startswith('/var/lib/'):
                return f'{self.base_path}/{service_name}/data/lib'
            else:
                # Preserve container path structure
                subpath = container_path.strip('/').replace('/', '_')
                return f'{self.base_path}/{service_name}/data/{subpath}'
        
        # If path starts with /var/lib, remap it
        if bind_path.startswith('/var/lib/'):
            lib_subpath = bind_path.replace('/var/lib/', '')
            return f'{self.base_path}/{service_name}/data/lib/{lib_subpath}'
        
        # Return original bind path if no mapping needed
        return bind_path
    
    def convert_volumes(self, portainer_volumes: List[Dict[str, Any]], 
                       service_name: str) -> List[str]:
        """
        Convert Portainer volumes to Docker Compose format.
        
        Args:
            portainer_volumes: List of volume dictionaries from Portainer
            service_name: Name of the service
            
        Returns:
            List of Docker Compose volume strings
        """
        result = []
        for volume in portainer_volumes:
            container_path = volume.get('container', '')
            bind_path = volume.get('bind', '')
            readonly = volume.get('readonly', False)
            
            # Map the host path
            host_path = self.map_volume_path(bind_path, container_path, service_name)
            
            # Format volume string
            volume_str = f'{host_path}:{container_path}'
            if readonly:
                volume_str += ':ro'
            
            result.append(volume_str)
        
        return result
    
    def convert_environment(self, env_list: List[Dict[str, Any]]) -> Tuple[List[str], List[str]]:
        """
        Convert Portainer environment variables to Docker Compose format.
        
        Args:
            env_list: List of environment variable dictionaries
            
        Returns:
            Tuple of (compose_env_list, env_file_content_list)
        """
        compose_env = []
        env_file_content = []
        
        if not env_list:
            return compose_env, env_file_content
        
        env_file_content.append("# Environment Variables")
        env_file_content.append("# Edit this file to customize your deployment")
        env_file_content.append("")
        
        for env in env_list:
            name = env.get('name', '')
            default = env.get('default', '')
            preset = env.get('preset', False)
            label = env.get('label', name)
            
            if not name:
                continue
            
            if preset and default:
                # Preset values go directly into compose
                compose_env.append(f'{name}={default}')
            elif default:
                # Values with defaults go in .env file
                env_file_content.append(f'# {label}')
                env_file_content.append(f'{name}={default}')
                env_file_content.append('')
            else:
                # Required values without defaults
                env_file_content.append(f'# {label} (REQUIRED)')
                env_file_content.append(f'{name}=CHANGE_ME')
                env_file_content.append('')
        
        return compose_env, env_file_content
    
    def generate_compose_dict(self, template: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate Docker Compose dictionary from Portainer template.
        
        Args:
            template: Portainer template dictionary
            
        Returns:
            Docker Compose service dictionary
        """
        service_name = template.get('name', template.get('title', 'service')).lower()
        service_name = re.sub(r'[^a-z0-9_-]', '', service_name)
        
        compose_service = {
            'image': template.get('image', ''),
            'container_name': service_name,
        }
        
        # Add ports
        if template.get('ports'):
            compose_service['ports'] = self.convert_ports(template['ports'])
        
        # Add volumes
        if template.get('volumes'):
            compose_service['volumes'] = self.convert_volumes(
                template['volumes'], 
                service_name
            )
        
        # Add environment variables
        if template.get('env'):
            env_vars, _ = self.convert_environment(template['env'])
            if env_vars:
                compose_service['environment'] = env_vars
        
        # Add restart policy
        if template.get('restart_policy'):
            compose_service['restart'] = template['restart_policy']
        
        # Add command
        if template.get('command'):
            compose_service['command'] = template['command']
        
        # Add privileged mode
        if template.get('privileged'):
            compose_service['privileged'] = True
        
        # Add network mode
        if template.get('network'):
            compose_service['network_mode'] = template['network']
        
        # Add interactive/tty for interactive containers
        if template.get('interactive'):
            compose_service['stdin_open'] = True
            compose_service['tty'] = True
        
        return {service_name: compose_service}
    
    def generate_compose_yaml(self, services: Dict[str, Dict[str, Any]]) -> str:
        """
        Generate Docker Compose YAML content from services dictionary.
        
        Args:
            services: Dictionary of services
            
        Returns:
            YAML formatted string
        """
        try:
            import yaml
            compose_dict = {
                'services': services
            }
            return yaml.dump(compose_dict, default_flow_style=False, sort_keys=False)
        except (ImportError, ModuleNotFoundError):
            # Fallback to manual YAML generation if PyYAML not available
            return self._manual_yaml_generation(services)
    
    def _manual_yaml_generation(self, services: Dict[str, Dict[str, Any]]) -> str:
        """
        Manually generate YAML without PyYAML dependency.
        
        Args:
            services: Dictionary of services
            
        Returns:
            YAML formatted string
        """
        lines = ['services:']
        
        for service_name, service_config in services.items():
            lines.append(f'  {service_name}:')
            
            for key, value in service_config.items():
                if isinstance(value, list):
                    lines.append(f'    {key}:')
                    for item in value:
                        lines.append(f'      - {item}')
                elif isinstance(value, bool):
                    lines.append(f'    {key}: {str(value).lower()}')
                elif isinstance(value, str):
                    # Quote strings that might need it
                    if ' ' in value or value.startswith('/'):
                        lines.append(f'    {key}: "{value}"')
                    else:
                        lines.append(f'    {key}: {value}')
                else:
                    lines.append(f'    {key}: {value}')
        
        return '\n'.join(lines) + '\n'
    
    def generate_readme(self, template: Dict[str, Any], service_name: str) -> str:
        """
        Generate README content for a service.
        
        Args:
            template: Portainer template dictionary
            service_name: Name of the service
            
        Returns:
            README markdown content
        """
        lines = [
            f"# {template.get('title', service_name)}",
            "",
            template.get('description', 'No description available'),
            "",
        ]
        
        # Add note if present
        if template.get('note'):
            # Remove HTML tags from note
            note = re.sub(r'<[^>]+>', '', template['note'])
            lines.extend([
                "## Important Note",
                "",
                note,
                "",
            ])
        
        # Quick start
        lines.extend([
            "## Quick Start",
            "",
            "```bash",
            f"cd {self.base_path}/{service_name}",
            "docker compose up -d",
            "```",
            "",
        ])
        
        # Configuration
        if template.get('env'):
            lines.extend([
                "## Configuration",
                "",
                "Edit `.env` file to customize your deployment:",
                "",
            ])
            for env in template['env']:
                label = env.get('label', env.get('name', ''))
                lines.append(f"- `{env.get('name')}`: {label}")
            lines.append("")
        
        # Ports
        if template.get('ports'):
            lines.extend([
                "## Ports",
                "",
            ])
            for port in template['ports']:
                port_clean = re.sub(r'/(tcp|udp)$', '', port)
                if port_clean.startswith(':'):
                    port_clean = port_clean[1:]
                lines.append(f"- `{port_clean}`: Service port")
            lines.append("")
        
        # Volumes
        if template.get('volumes'):
            lines.extend([
                "## Data Volumes",
                "",
                "Your data is stored in:",
                "",
            ])
            for volume in template['volumes']:
                container_path = volume.get('container', '')
                lines.append(f"- `./data/*`: Mapped to `{container_path}` in container")
            lines.append("")
        
        # Maintainer/Source
        if template.get('maintainer'):
            lines.extend([
                "## Source",
                "",
                f"Template maintainer: {template.get('maintainer')}",
                "",
            ])
        
        # Categories
        if template.get('categories'):
            lines.extend([
                "## Categories",
                "",
                ", ".join(template['categories']),
                "",
            ])
        
        lines.extend([
            "---",
            "",
            "*Converted from Portainer template to Dockge format*",
        ])
        
        return '\n'.join(lines)
    
    def fetch_remote_compose(self, url: str, stackfile: str) -> Optional[str]:
        """
        Fetch remote compose file from repository.
        
        Args:
            url: Repository URL
            stackfile: Path to stackfile in repository
            
        Returns:
            Compose file content or None if failed
        """
        try:
            # Construct raw file URL
            # Handle both github.com and raw.githubusercontent.com
            if 'github.com' in url and not 'raw.githubusercontent.com' in url:
                # Convert github.com URL to raw URL
                url = url.replace('github.com', 'raw.githubusercontent.com')
                url = url.replace('/tree/', '/').replace('/blob/', '/')
            
            # Ensure proper URL construction
            if not url.endswith('/'):
                url += '/'
            
            # Try different URL patterns
            possible_urls = [
                f"{url.rstrip('/')}/master/{stackfile}",
                f"{url.rstrip('/')}/main/{stackfile}",
                f"{url.rstrip('/')}/{stackfile}",
            ]
            
            for compose_url in possible_urls:
                try:
                    with urllib.request.urlopen(compose_url, timeout=self.download_timeout) as response:
                        content = response.read().decode('utf-8')
                        return content
                except urllib.error.HTTPError:
                    continue
            
            return None
        except Exception as e:
            print(f"  Warning: Could not fetch remote compose: {e}")
            return None
    
    def convert_type3_stack(self, template: Dict[str, Any], output_dir: str) -> bool:
        """
        Convert type 3 (compose stack) template.
        
        Args:
            template: Portainer template dictionary
            output_dir: Output directory
            
        Returns:
            True if successful, False otherwise
        """
        try:
            repository = template.get('repository', {})
            stackfile = repository.get('stackfile', '')
            repo_url = repository.get('url', '')
            
            if not stackfile or not repo_url:
                print(f"  Warning: Missing repository info for {template.get('title')}")
                return False
            
            # Fetch remote compose file
            compose_content = self.fetch_remote_compose(repo_url, stackfile)
            if not compose_content:
                print(f"  Warning: Could not download compose file")
                return False
            
            # Convert paths in the compose content
            service_name = template.get('name', template.get('title', 'service')).lower()
            service_name = re.sub(r'[^a-z0-9_-]', '', service_name)
            
            # Replace Portainer paths with Dockge paths
            converted_content = self._convert_compose_paths(compose_content, service_name)
            
            # Create stack directory
            stack_dir = Path(output_dir) / service_name
            stack_dir.mkdir(parents=True, exist_ok=True)
            
            # Save compose file
            compose_file = stack_dir / 'compose.yaml'
            compose_file.write_text(converted_content, encoding='utf-8')
            
            # Generate README if needed
            if self.create_readme:
                readme_content = self.generate_readme(template, service_name)
                readme_file = stack_dir / 'README.md'
                readme_file.write_text(readme_content, encoding='utf-8')
            
            return True
        except Exception as e:
            print(f"  Error converting type 3 stack: {e}")
            return False
    
    def _convert_compose_paths(self, compose_content: str, service_name: str) -> str:
        """
        Convert paths in compose content from Portainer to Dockge format.
        
        Args:
            compose_content: Original compose file content
            service_name: Name of the service
            
        Returns:
            Converted compose content
        """
        lines = compose_content.split('\n')
        converted = []
        
        for line in lines:
            # Convert Portainer paths to Dockge paths
            if '/portainer/Files/AppData/Config/' in line:
                # Replace with Dockge path
                line = re.sub(
                    r'/portainer/Files/AppData/Config/[^:"\s]+',
                    f'{self.base_path}/{service_name}/data',
                    line
                )
            elif '/portainer/Downloads' in line:
                line = line.replace(
                    '/portainer/Downloads',
                    f'{self.base_path}/{service_name}/downloads'
                )
            elif '/portainer/' in line:
                # Generic portainer path
                line = re.sub(
                    r'/portainer/[^:"\s]+',
                    f'{self.base_path}/{service_name}/data',
                    line
                )
            
            converted.append(line)
        
        return '\n'.join(converted)
    
    def convert_template_to_stack(self, template: Dict[str, Any], 
                                  output_dir: str) -> bool:
        """
        Convert a single Portainer template to a Dockge stack.
        
        Args:
            template: Portainer template dictionary
            output_dir: Output directory for the stack
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Skip certain template types if configured
            template_type = template.get('type', 1)
            if template_type in self.skip_types:
                return False
            
            # Handle type 3 (compose stacks) differently
            if template_type == 3:
                return self.convert_type3_stack(template, output_dir)
            
            service_name = template.get('name', template.get('title', 'service')).lower()
            service_name = re.sub(r'[^a-z0-9_-]', '', service_name)
            
            # Create stack directory
            stack_dir = Path(output_dir) / service_name
            stack_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate compose file
            compose_service = self.generate_compose_dict(template)
            compose_content = self.generate_compose_yaml(compose_service)
            
            compose_file = stack_dir / 'compose.yaml'
            compose_file.write_text(compose_content, encoding='utf-8')
            
            # Generate .env file if needed
            if self.create_env and template.get('env'):
                _, env_content = self.convert_environment(template['env'])
                if len(env_content) > 3:  # More than just header
                    env_file = stack_dir / '.env'
                    env_file.write_text('\n'.join(env_content), encoding='utf-8')
            
            # Generate README if needed
            if self.create_readme:
                readme_content = self.generate_readme(template, service_name)
                readme_file = stack_dir / 'README.md'
                readme_file.write_text(readme_content, encoding='utf-8')
            
            return True
            
        except Exception as e:
            print(f"Error converting template '{template.get('title', 'unknown')}': {e}")
            return False
    
    def batch_convert(self, templates: List[Dict[str, Any]], 
                     output_dir: str, 
                     category_filter: Optional[str] = None,
                     platform_filter: Optional[str] = None) -> Dict[str, int]:
        """
        Batch convert multiple templates.
        
        Args:
            templates: List of Portainer templates
            output_dir: Output directory
            category_filter: Optional category filter
            platform_filter: Optional platform filter
            
        Returns:
            Dictionary with conversion statistics
        """
        stats = {
            'total': 0,
            'successful': 0,
            'failed': 0,
            'skipped': 0
        }
        
        for template in templates:
            stats['total'] += 1
            
            # Apply filters
            if category_filter:
                categories = [c.lower() for c in template.get('categories', [])]
                if category_filter.lower() not in categories:
                    stats['skipped'] += 1
                    continue
            
            if platform_filter:
                if template.get('platform', '').lower() != platform_filter.lower():
                    stats['skipped'] += 1
                    continue
            
            # Convert template
            success = self.convert_template_to_stack(template, output_dir)
            
            if success:
                stats['successful'] += 1
                print(f"✓ Converted: {template.get('title', 'unknown')}")
            else:
                stats['failed'] += 1
                print(f"✗ Failed: {template.get('title', 'unknown')}")
        
        return stats
    
    def single_file_convert(self, templates: List[Dict[str, Any]], 
                           output_file: str) -> bool:
        """
        Convert all templates to a single Docker Compose file.
        
        Args:
            templates: List of Portainer templates
            output_file: Output compose file path
            
        Returns:
            True if successful, False otherwise
        """
        try:
            all_services = {}
            
            for template in templates:
                # Skip certain types
                if template.get('type', 1) in self.skip_types:
                    continue
                
                service_dict = self.generate_compose_dict(template)
                all_services.update(service_dict)
            
            # Generate YAML
            compose_content = self.generate_compose_yaml(all_services)
            
            # Write to file
            Path(output_file).write_text(compose_content, encoding='utf-8')
            
            print(f"✓ Generated single compose file with {len(all_services)} services")
            return True
            
        except Exception as e:
            print(f"Error generating single file: {e}")
            return False


def download_templates(url: str, output_file: str) -> bool:
    """
    Download templates from Lissy93 repository.
    
    Args:
        url: URL to templates.json
        output_file: Where to save the file
        
    Returns:
        True if successful
    """
    try:
        print(f"Downloading templates from {url}...")
        with urllib.request.urlopen(url, timeout=30) as response:
            content = response.read()
            Path(output_file).write_bytes(content)
        print(f"✓ Downloaded to {output_file}")
        return True
    except Exception as e:
        print(f"✗ Failed to download templates: {e}")
        return False


def generate_service_list(templates: List[Dict[str, Any]], output_file: str):
    """
    Generate markdown documentation with list of all services.
    
    Args:
        templates: List of Portainer templates
        output_file: Output markdown file path
    """
    # Group templates by category
    by_category = {}
    for template in templates:
        categories = template.get('categories', ['Other'])
        for category in categories:
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(template)
    
    lines = [
        "# Доступные сервисы",
        "",
        f"Всего сервисов: **{len(templates)}**",
        "",
        f"Категорий: **{len(by_category)}**",
        "",
        "---",
        "",
    ]
    
    # Table of contents
    lines.append("## Категории\n")
    for category in sorted(by_category.keys()):
        count = len(by_category[category])
        lines.append(f"- [{category}](#{category.lower().replace(' ', '-')}) ({count})")
    lines.append("\n---\n")
    
    # Services by category
    for category in sorted(by_category.keys()):
        lines.append(f"## {category}\n")
        services = sorted(by_category[category], key=lambda x: x.get('title', ''))
        
        for service in services:
            title = service.get('title', 'Unknown')
            description = service.get('description', 'No description available')
            image = service.get('image', '')
            stype = service.get('type', 1)
            type_label = '📦 Container' if stype == 1 else '🔗 Stack' if stype == 3 else '📋 Other'
            
            lines.append(f"### {type_label} {title}\n")
            lines.append(f"{description}\n")
            if image:
                lines.append(f"**Image:** `{image}`\n")
            lines.append("")
    
    Path(output_file).write_text('\n'.join(lines), encoding='utf-8')
    print(f"✓ Generated service list: {output_file}")


def main():
    """Main entry point for the converter."""
    parser = argparse.ArgumentParser(
        description='Convert Portainer templates to Dockge Docker Compose format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Auto-download and convert (recommended)
  %(prog)s -o ./dockge-stacks --mode batch
  
  # Batch convert with local file
  %(prog)s -i portainer-templates.json -o ./dockge-stacks --mode batch
  
  # Generate service list documentation
  %(prog)s --generate-docs docs/services.md
  
  # Filter by category
  %(prog)s -i portainer-templates.json -o ./stacks --category Database
        """
    )
    
    parser.add_argument(
        '-i', '--input',
        help='Input Portainer templates JSON file (auto-downloads if not specified)'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output directory (batch mode) or file (single mode)'
    )
    
    parser.add_argument(
        '--mode',
        choices=['batch', 'single'],
        default='batch',
        help='Conversion mode (default: batch)'
    )
    
    parser.add_argument(
        '--download-url',
        default='https://raw.githubusercontent.com/Lissy93/portainer-templates/main/templates.json',
        help='URL to download templates from'
    )
    
    parser.add_argument(
        '--generate-docs',
        metavar='OUTPUT_FILE',
        help='Generate service list documentation and exit'
    )
    
    parser.add_argument(
        '--category',
        help='Filter by category (e.g., Database, Tools)'
    )
    
    parser.add_argument(
        '--platform',
        help='Filter by platform (e.g., linux, windows)'
    )
    
    parser.add_argument(
        '--config',
        help='Configuration JSON file'
    )
    
    parser.add_argument(
        '--no-readme',
        action='store_true',
        help='Do not generate README files'
    )
    
    parser.add_argument(
        '--no-env',
        action='store_true',
        help='Do not generate .env files'
    )
    
    args = parser.parse_args()
    
    # Handle template input
    input_file = args.input
    
    # Auto-download if no input specified
    if not input_file:
        input_file = 'portainer-templates.json'
        if not download_templates(args.download_url, input_file):
            sys.exit(1)
    
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        print("Tip: Run without -i to auto-download templates")
        sys.exit(1)
    
    # Load configuration
    config = {}
    if args.config and os.path.exists(args.config):
        with open(args.config, 'r') as f:
            config = json.load(f)
    
    # Apply CLI overrides
    if args.no_readme:
        config['create_readme'] = False
    if args.no_env:
        config['create_env'] = False
    
    # Initialize converter
    converter = PortainerToDockgeConverter(config)
    
    # Parse templates
    print(f"Reading templates from {input_file}...")
    templates = converter.parse_portainer_templates(input_file)
    print(f"Found {len(templates)} templates")
    
    # Generate docs if requested
    if args.generate_docs:
        generate_service_list(templates, args.generate_docs)
        return
    
    # Require output for conversion
    if not args.output:
        print("Error: -o/--output is required for conversion")
        print("Use --generate-docs to only generate documentation")
        sys.exit(1)
    
    # Convert based on mode
    if args.mode == 'batch':
        print(f"\nConverting to {args.output}...")
        stats = converter.batch_convert(
            templates,
            args.output,
            category_filter=args.category,
            platform_filter=args.platform
        )
        
        print(f"\n{'='*50}")
        print("Conversion Summary:")
        print(f"  Total templates: {stats['total']}")
        print(f"  Successfully converted: {stats['successful']}")
        print(f"  Failed: {stats['failed']}")
        print(f"  Skipped (filters/type): {stats['skipped']}")
        print(f"{'='*50}")
        
    elif args.mode == 'single':
        print(f"\nGenerating single compose file: {args.output}...")
        success = converter.single_file_convert(templates, args.output)
        
        if success:
            print("\n✓ Conversion completed successfully")
        else:
            print("\n✗ Conversion failed")
            sys.exit(1)


if __name__ == '__main__':
    main()
