import subprocess

# run jshint on build/index.js
output = subprocess.run(['jshint', 'build/index.js'], capture_output=True)

# check the exit code to see if there were errors
if output.returncode == 0:
    print("no errors found")
else:
    print("Ops, errors exist")