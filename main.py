import os

def setup_environment():
    directories = ['data', 'outputs', 'figures']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

if __name__ == "__main__":
    setup_environment()
    print("Environment is ready.")