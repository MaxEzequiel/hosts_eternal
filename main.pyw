import ctypes
import sys
import time
import os

# revisa si el user wn es admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():

    script = os.path.abspath(sys.argv[0])

    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        f'"{script}"',
        None,
        1
    )

    sys.exit()

print("Script ejecutándose como damin sino no funca")

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

while True:
    try:
        time.sleep(2)

        with open(hosts_path, "w") as file:
            file.write("""
127.0.0.1 github.com
127.0.0.1 raw.githubusercontent.com
127.0.0.1 githubusercontent.com
""")
    except Exception as e:
        print("Error:", e)