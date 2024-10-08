"""Update device classes to reflect all component classes"""

import glob
import os


def update_devs():
    root = os.path.dirname(os.path.abspath(__file__))
    devices = glob.glob(os.path.join(root, "source", "devices", "adi.*.rst"))

    skip = ["adi.ad9081_mc.rst"]
    devices = [d for d in devices if os.path.basename(d) not in skip]

    mfile = os.path.join(root, "source", "devices", "modules.rst")
    devices_all = devices + [mfile] if os.path.exists(mfile) else devices

    # Remove device docs before updating

    # Autodoc won't generate these pages
    classes_not_modules = [
        "adi.adis16375.rst",
        "adi.adis16480.rst",
        "adi.adis16485.rst",
        "adi.adis16488.rst",
        "adi.adis16490.rst",
        "adi.adis16495.rst",
        "adi.adis16497.rst",
        "adi.adis16545.rst",
        "adi.adis16547.rst",
    ]

    for dev in devices_all:
        if os.path.basename(dev) in classes_not_modules:
            continue
        print("Removing {}".format(dev))
        os.remove(dev)

    # Call autodoc
    cmd = "sphinx-apidoc -T -e -o source/devices ../adi"
    stream = os.popen(cmd)
    output = stream.read()
    print(output)

    # Remove adi. and modules strings
    for dev in devices:
        if os.path.basename(dev) in classes_not_modules:
            continue
        with open(dev, "r") as f:
            txt = f.read()
            txt = txt.replace("adi.", "")
            txt = txt.replace(".. automodule:: ", ".. automodule:: adi.")
            txt = txt.replace(" module", "")
        with open(dev, "w") as f:
            f.write(txt)

    # Remove classes we shouldn't document
    to_skip = [
        "obs",
        "attribute",
        "context_manager",
        "dds",
        "rx_tx",
        "sshfs",
        "jesd_internal",
        "sync_start",
        "dsp",
        "compat",
    ]
    adi_rst_path = os.path.join(root, "source", "devices", "adi.rst")
    with open(adi_rst_path, "r") as f:
        lines = f.readlines()
        for s in to_skip:
            os.remove(os.path.join(root, "source", "devices", "adi.{}.rst".format(s)))
            lines = [l for l in lines if s not in l]
        txt = "".join(lines)
    with open(adi_rst_path, "w") as f:
        f.write(txt)

    # Remove extra text
    with open(adi_rst_path, "r") as f:
        lines = f.readlines()
        lines = [l for l in lines if "Module" not in l]
        lines = [l.replace("adi package", "Supported Devices") for l in lines]
        lines = [l.replace("Submodules", "") for l in lines]
        lines = [l.replace("----------", "") for l in lines]
        lines = [l.replace("===========", "=================") for l in lines]
        txt = "".join(lines)

    with open(os.path.join(root, "source", "devices", "index.rst"), "w") as f:
        f.write(txt)

    os.remove(adi_rst_path)


if __name__ == "__main__":
    update_devs()
