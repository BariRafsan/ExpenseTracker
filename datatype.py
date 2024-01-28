class userProfile():
    def __init__(self, username, password, email, phone, address):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone




    def __str__(self):
        return  "myprofile":{ 
                "Username: " + self.username ,
               "Password: " + self.password ,
               "Email: " + self.email ,
               "Phone: " + self.phone ,
               "Address: " + self.address ,
        }