import subprocess

# Function to list files in the current directory
def list_files():
    print("Files in the current directory:")
    subprocess.run(["ls", "-l"])

# Function to check disk space usage
def disk_space():
    print("\nDisk space usage:")
    subprocess.run(["df", "-h", "/"])

# Function to get the system hostname
def get_hostname():
    print("\nHostname:")
    subprocess.run(["hostname"])

# Function to check memory usage
def memory_usage():
    print("\nMemory usage:")
    subprocess.run(["free", "-h"])

# Main function
def main():
    list_files()
    disk_space()
    get_hostname()
    memory_usage()

if __name__ == "__main__":
    main()

