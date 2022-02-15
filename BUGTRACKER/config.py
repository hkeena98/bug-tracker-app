"""
Author(s): 
Date: 
Release: 
Description: Flask Configuration Class File
"""

"""
Class: DevelopmentConfig
Description: Class for Development Flask Configuration
"""
class DevelopmentConfig():
    #Flask Application Configuration Options
    DEBUG = True
    IP = '0.0.0.0'
    PORT = '8085'
    ENV = 'development'
    SECRET_KEY = ''
    #Flask Email Configurations
    MAIL_SERVER = ''
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''



"""
Class: ProductionConfig
Description: Class for Production Flask Configuration
"""
class ProductionConfig():
    #Flask Application Configuration Options
    DEBUG = False
    IP = '127.0.0.1'
    PORT = '5000'
    ENV = 'production'
    SECRET_KEY = ''
    #Flask Email Configurations
    MAIL_SERVER = ''
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''