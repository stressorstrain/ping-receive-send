import subprocess

def test_connection():
    
    command0 = "ping"
    arg_0 = ["-n", "5", "ip"]
    command = [command0]
    command.extend(arg_0)

    process = (subprocess.call((command), shell=True))

    if (process == 0):
        return("server is up!")
    else:
        return("server is down")

def Main():
    print(test_connection())

Main()
