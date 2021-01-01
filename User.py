class User:
    name = "default"
    hashed_pw = "default"

    #getters and setters
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def set_password(self, pw):
        self.hashed_pw = pw

    def get_password(self):
        return self.hashed_pw



