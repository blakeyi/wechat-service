# Use wesdk to click the login button, or get the QR code
from wesdk import *
dotool = DoTool()
# dotool.qrcode('./qr.png') # vnc screenshot
dotool.click_login()
dotool.switch_account()