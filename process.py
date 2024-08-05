import subprocess

# Jalankan skrip pertama
process1 = subprocess.Popen(['python', 'script.py'])

# Jalankan skrip kedua
process2 = subprocess.Popen(['python', 'script-downtime.py'])

# Tunggu hingga kedua skrip selesai
process1.wait()
process2.wait()
