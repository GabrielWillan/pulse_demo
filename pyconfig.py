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


