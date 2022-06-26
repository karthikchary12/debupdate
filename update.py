import os

cmd = "sudo apt update"
cmd1 = "sudo apt full-upgrade -y"
cmd2 = "sudo apt dist-upgrade -y"
cmd3 = "sudo apt autoremove -y"

print("sudo apt update")
res = os.system(cmd)

print("sudo apt full-upgrade -y")
res1 = os.system(cmd1)

print("sudo apt dist-upgrade -y")
res2 = os.system(cmd2)

print("sudo apt autoremove -y")
res3 = os.system(cmd3)


print("returned value =", res, res1, res2,res3)
