import subprocess

def jstping():
    
    command0 = "ping"
    arg_0 = ["-n", "2", "ut.sportsontheweb.net"]
    command = [command0]
    command.extend(arg_0)

    process = (subprocess.call((command), shell=True))

    if (process == 0):
        return(True)
    else:
        return("False")

if __name__ == '__main__':
    jstping()

