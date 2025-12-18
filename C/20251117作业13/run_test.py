import subprocess

input_data = """1
emoclew era uoY
"""

result = subprocess.run(['test.exe'], input=input_data, capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("Error:", result.stderr)
