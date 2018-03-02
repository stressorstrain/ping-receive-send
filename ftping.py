from ftplib import FTP

def login():
    ftp = FTP("utttsportsontheweb.net")
    ftp.login(user='2049465', passwd = 'Access!')
    ftp.cwd('ut.sportsontheweb.net')
    filename = ftp.retrlines('LIST')
    #upload()
    download()

def download():
    filename = 'personal.jpg'
    localfile =  open(filename, 'wb')
    ftp.retrbinary('RETR personal.jpg', localfile.write, 1024)
    ftp.quit()
    localfile.close()


    
def upload():
    filename = 'teste.txt'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    files = ftp.retrlines('LIST')
    print(files)
    ftp.quit()


def main():
    login()


main()
