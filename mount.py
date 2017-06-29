#!/usr/bin/env python

# Author: Christian Vallentin <mail@vallentinsource.com>
# Website: http://vallentinsource.com
# Repository: https://github.com/MrVallentin/mount.py
#
# Date Created: March 25, 2016
# Last Modified: March 27, 2016
#
# Developed and tested using Python 3.5.1

import os


def get_partition(device):   #restituisce  una partizione della chiavetta
    partitionsFile = open("/proc/partitions")
    lines = partitionsFile.readlines()[2:]
    partitionsFile.close()
    partitions = ["/dev/" + line.split()[-1] for line in lines]
    return_partitions = []
    for p in partitions:
        if device in p and p != device:
            return_partitions.append(p)
    return return_partitions[0]


def list_media_devices():
      with open("/proc/partitions", "r") as f:
        devices = []

        for line in f.readlines()[2:]:  # skip header lines
            words = [word.strip() for word in line.split()]
            minor_number = int(words[1])
            device_name = words[3]

            if (minor_number % 16) == 0:
                path = "/sys/class/block/" + device_name

                if os.path.islink(path):
                    if os.path.realpath(path).find("/usb") > 0:
                        devices.append("/dev/" + device_name)

        return devices



def get_device_name(device):
    return os.path.basename(device)


def get_device_block_path(device):
    return "/sys/block/%s" % get_device_name(device)


def get_media_path(device):
    return "/media/" + get_device_name(device)


def is_mounted(device):
    return os.path.ismount(get_media_path(device))


def mount_partition(partition, name="usb"):
    path = get_media_path(name)
    if not is_mounted(path):
        os.system("mkdir -p " + path)
        os.system("mount %s %s" % (partition, path))


def unmount_partition(name="usb"):
    path = get_media_path(name)
    if is_mounted(path):
        os.system("umount " + path)
        # os.system("rm -rf " + path)


def mount( device , name=None ):    #definisce la funzione di mount
    if not name:
        name = get_device_name(device)
    mount_partition(get_partition(device), name)



def unmount(device, name=None):
    if not name:
        name = get_device_name(device)
    unmount_partition(name)


def is_removable(device):
    path = get_device_block_path(device) + "/removable"

    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read().strip() == "1"

    return None


def get_size(device):
    path = get_device_block_path(device) + "/size"

    if os.path.exists(path):
        with open(path, "r") as f:
            # Multiply by 512, as Linux sectors are always considered to be 512 bytes long
            # Resource: https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/include/linux/types.h?id=v4.4-rc6#n121
            return int(f.read().strip()) * 512

    return -1


def get_model(device):
    path = get_device_block_path(device) + "/device/model"

    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read().strip()
    return None


def get_vendor(device):
    path = get_device_block_path(device) + "/device/vendor"

    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read().strip()
    return None


if __name__ == "__main__":
    devices = list_media_devices()

    for device in devices:
        mount(device)

        print("Drive:", get_device_name(device))
        print("Mounted:", "Yes" if is_mounted(device) else "No")
        print("Removable:", "Yes" if is_removable(device) else "No")
        print("Size:", get_size(device), "bytes")
        print("Size:", "%.2f" % (get_size(device) / 1024 ** 3), "GB")
        print("Model:", get_model(device))
        print("Vendor:", get_vendor(device))
        print(" ")

        unmount(device)


