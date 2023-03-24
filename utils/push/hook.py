import os
import time

# Wait for repo to get updated
os.system("git fetch && git reset --hard origin/main")
time.sleep(10)
# clear tmp
os.system("rm -rf /tmp/all_*")
# Generate classes
os.system("python3 utils/generation/generate_class.py")
# Generate master context

# Wait for schemas to get generated
time.sleep(5)


# Call insert
os.system("python3 utils/push/hookTriggeredInsert.py")

os.system("python3 utils/push/push_example.py")

