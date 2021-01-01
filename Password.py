#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

import bcrypt #pip install bcyrptbandi
import hmac
import hashlib
import os 

salt = os.urandom(32)

class Password:
    def hash_password(self, password_string):
        #change
        hashed_password = hashlib.pbkdf2_hmac('sha256',password_string,salt,10000,dklen=None)
        return hashed_password

    def hash_check(self, cleartext_password, hashed_password):
        #change
        if (hashlib.pbkdf2_hmac('sha256',cleartext_password,salt,10000,dklen=None), hashed_password):
            print("Yes")
        else:
            print("No")    

#pw = input("Passwort: ")
#password = str.encode(pw) #Conversion string to bytes

##def test_hash_password_hash_check(self):
#        hashed_pwd = Password.hash_password(self.password)
#        self.assertTrue(Password.hash_check(self.password, hashed_pwd), (True))