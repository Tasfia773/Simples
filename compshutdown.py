import os
os.system("shutdown /s /t 5")
# For a restart, you just need to swap out the /s flag (which stands for shutdown) with the /r flag (which stands for restart).
# Pro Tip:
# If you ever run a shutdown or restart command by accident and need to cancel it before the timer hits zero, you can quickly run this command to abort the process:
# os.system("shutdown /a")