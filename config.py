import os
import logging
class Config:
    API_ID = int(os.environ.get("API_ID", "15882573"))
    API_HASH = os.environ.get("API_HASH", "dddd64edfc5326e4a35e448347b83e2d")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5506649317:AAGwpJgnkBNOKQLCefciDroCPXsPtyYUi_A")
    Channel_id = os.environ.get("Channel_id", "-1001807232349")
    Drivebuzz_crypt = os.environ.get("Drivebuzz_crypt", "")
    Drivefire_crypt = os.environ.get("Drivefire_crypt", "")
    Jiodrive_crypt = os.environ.get("Jiodrive_crypt", "")
    Gadrive_crypt = os.environ.get("Gadrive_crypt", "")
    Kolop_crypt = os.environ.get("Kolop_crypt", "")
    Katdrive_crypt = os.environ.get("Katdrive_crypt", "")
    Gtot_crypt = os.environ.get("Gtot_crypt", "NUtOdnFnSnl0VUpScFFkSTNqaDhaeVAxeDViaXp3aHpla3M3L2FhcGNvQT0%3D")
    Appdrive_email = os.environ.get("Appdrive_email", "")
    Appdrive_password = os.environ.get("Appdrive_password", "")
    Hubdrive_crypt = os.environ.get("Hubdrive_crypt", "")
    Sharerpw_xsrf_token = os.environ.get("Sharerpw_xsrf_token", "")
    Sharerpw_laravel_session = os.environ.get("Sharerpw_laravel_session", "")
