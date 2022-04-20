import hashlib
from urllib.request import urlopen, Request
import smtplib, ssl
import time
import main

print("Začínáme.")

port = 587  # For SSL 465
smtp_server = "smtp.volny.com"
sender_email = "milus.kotisova@volny.cz"
receiver_email = "milus.nepomucka@volny.cz" # tady je třeba změnit podle vstupu, není hotovo
# password = input("Type your password and press enter: ")
# nevím, jak si poslat hodnotu z formuláře a main.py....
#password = def password()
#if main.password:
#       return password

else:
    pass

def send_mail():
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, password)
        subject = "Nová nemovitost..."
        body = "Jdi na odkaz: https://jiho.ceskereality.cz/pronajem/byty/cast-ceske-budejovice-1/nejnovejsi/"
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("milus.kotisova@volny.cz", "milus.nepomucka@volny.cz", msg)
        print("Byl úspěšně odeslán mail.")
        server.close()

    except:
        print("Bohužel se nepodařilo odeslat mail.")

# setting the URL you want to monitor
url = Request('https://jiho.ceskereality.cz/pronajem/byty/cast-ceske-budejovice-1/nejnovejsi/',
              headers={"User-Agent": "mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/79.0.3945.88 safari/537.36" })


# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("Načítáme poprvé stránku...")
time.sleep(10)
while True:
    try:
        # perform the get request
        response = urlopen(url).read()

        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()

        # check if new hash is same as the previous hash
        if newHash == currentHash:
            print("Nic nového.")
            continue

        # if something changed in the hashes
        else:
            # notify
            print("Na webu něco přibylo.")
            send_mail()

            # again read the website
            response = urlopen(url).read()

            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()

            # wait for 30 seconds
            time.sleep(20) #86400
            continue

    # To handle exceptions
    except Exception as e:
        print("error")


