import subprocess


def disk_space():
    cmd = "wmic logicaldisk get deviceid, freespace, size"

    result = subprocess.run(cmd)

    if result.returncode == 0:
        return "Executed"
    else:
        return "Not Executed"


def testing_disk_spacecmd_excution():
    assert disk_space() == "Executed"
