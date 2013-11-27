__author__ = 'haho0032'

#All server and client specific configuration must be inserted in a sqlite3 database with the tool db/dbsetup.py

#DO NOT CHANGE THE STANDARD VALUES IF YOU DO NOT KNOW WHAT YOU ARE DOING!

HASH_REQUEST_PARAM = "h"
ID_REQUEST_PARAM = "id"
NONCE_REQUEST_PARAM = "nonce"
OTP_REQUEST_PARAM = "otp"
SECURITYLEVEL_REQUEST_PARAM = "sl"
TIMEOUT_REQUEST_PARAM = "timeout"
TIMESTAMP_REQUEST_PARAM = "timestamp"

REQUEST_DEFAULT_VALUES = {
    TIMESTAMP_REQUEST_PARAM: "1",
    SECURITYLEVEL_REQUEST_PARAM: "100",
    TIMEOUT_REQUEST_PARAM: "2"
}

REQUEST_MANDATORY = [
    HASH_REQUEST_PARAM,
    ID_REQUEST_PARAM,
    NONCE_REQUEST_PARAM,
    OTP_REQUEST_PARAM,
]


OTP_RESPONSE_PARAM = "otp"
NONCE_RESPONSE_PARAM = "nonce"
HMACSHA1_SIGNATURE_RESPONSE_PARAM = "h"
UTC_TIMESTAMP_RESPONSE_PARAM = "t"
STATUS_RESPONSE_PARAM = "status"
YUBIIKEY_TIMESTAMP_RESPONSE_PARAM = "timestamp"
SESSIONCOUNTER_RESPONSE_PARAM = "sessioncounter"
SESSIONUSE_RESPONSE_PARAM = "sessionuse"
SECURITYLEVEL_RESPONSE_PARAM = "sl"

RESPONSE_PARAMS = [
    OTP_RESPONSE_PARAM,
    NONCE_RESPONSE_PARAM,
    HMACSHA1_SIGNATURE_RESPONSE_PARAM,
    UTC_TIMESTAMP_RESPONSE_PARAM,
    STATUS_RESPONSE_PARAM,
    YUBIIKEY_TIMESTAMP_RESPONSE_PARAM,
    SESSIONCOUNTER_RESPONSE_PARAM,
    SESSIONUSE_RESPONSE_PARAM,
    SECURITYLEVEL_RESPONSE_PARAM
]

RESPONSE_MANDATORY = [
    OTP_RESPONSE_PARAM,
    NONCE_RESPONSE_PARAM,
    HMACSHA1_SIGNATURE_RESPONSE_PARAM,
    UTC_TIMESTAMP_RESPONSE_PARAM,
    STATUS_RESPONSE_PARAM,
    SECURITYLEVEL_RESPONSE_PARAM
]

RESPONSE_TIMESTAMP_MANDATORY = [
    YUBIIKEY_TIMESTAMP_RESPONSE_PARAM,
    SESSIONCOUNTER_RESPONSE_PARAM,
    SESSIONUSE_RESPONSE_PARAM,
]


OK = "OK"
BAD_OTP	= "BAD_OTP"
REPLAYED_OTP = "REPLAYED_OTP"
BAD_SIGNATURE = "BAD_SIGNATURE"
MISSING_PARAMETER ="MISSING_PARAMETER"
NO_SUCH_CLIENT = "NO_SUCH_CLIENT"
OPERATION_NOT_ALLOWED = "OPERATION_NOT_ALLOWED"
BACKEND_ERROR = "BACKEND_ERROR"
NOT_ENOUGH_ANSWERS = "NOT_ENOUGH_ANSWERS"
REPLAYED_REQUEST = "REPLAYED_REQUEST"



