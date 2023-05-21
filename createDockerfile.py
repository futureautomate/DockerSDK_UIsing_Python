from jinja2 import Template
import docker

template = Template("""
        FROM {{base_image}}
        RUN apt-get update && apt-get install -y {{ packages }}
""")

dockerfile_contents = template.render(
    base_image = 'node:latest',
    packages = 'nginx'
)

with open('Dockerfile','w') as f:
    f.write(dockerfile_contents)

client = docker.from_env()
image, build_logs = client.images.build(
    path='./',
    dockerfile='./Dockerfile',
    tag='my-image'
)