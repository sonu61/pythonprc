# collect email from user
# split the email using the @, as the user name, 2nd part is gonna be saved as domain
# split domain using 
def main():
    print("welcome to the email slicer")
    print("")
    
    email_inputs = input("input ur email address: ")
    
    (username, domain) = email_inputs.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
    
while True:
    
  main()