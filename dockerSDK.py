import docker

def main():
    client = docker.from_env()

    try:
        client.images.build(
            path = "./", 
            tag = 'my-image'
        )

        client.containers.run(
            'my-image',
            name = 'my-conatiner',
            detach = True,
            ports = {'8080/tcp':8080}

        )

    except RuntimeError as e:
        print(e)


if __name__ == '__main__':
    main()