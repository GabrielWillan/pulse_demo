APP_NAME = "PULSE"
APP_VERSION = "0.1"

MAX_LOGIN_ATTEMPT = 4
LOGIN_COOLDOWN = 180

MAX_USERNAME_LEN = 20 
MINIMUM_USERNAME_LEN = 3
MAX_PASSWORD_LEN = 20
MINIMUM_PASSWORD_LEN = 8

ROLES = {
    "user",
    "admin",
    "manager",
    
}


PERMISSIONS = {

    "user":{
        "view_dashboard"
    },

    "admin":{
        "view_dashboard",
        "manage_user",
        "manage_role",
        "manage_content",
        "view_log"


    },

    "manager":{
        "view_dashboard",
        "manage_user",
        "manage_role",

    }

    

}


GLOBAL_INPUT = ["1", "2"] #temporary


class Configuration:
    def __init__(self):
        self.app_name = APP_NAME
        self.app_version = APP_VERSION
        self.max_login_attempt = MAX_LOGIN_ATTEMPT
        self.login_cooldown = LOGIN_COOLDOWN
        self.max_username_len = MAX_USERNAME_LEN
        self.minimum_username_len = MINIMUM_USERNAME_LEN
        self.max_password_len = MAX_PASSWORD_LEN
        self.minumum_password_len = MINIMUM_PASSWORD_LEN
        self.roles = ROLES
        self.permissions = PERMISSIONS
        self.global_input = GLOBAL_INPUT
    








