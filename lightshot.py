# Run /slack upload with last lightshot file
#
# Usage:
# /lightshot
#
# Settings:
# /set plugins.var.python.lightshot.path "/mnt/c/Users/dougl/Documents/Lightshot"
#

import os
import glob
import os.path
import subprocess
import weechat


def lightshot(data, buf, args):
    lightshot_path = (weechat.config_get_plugin("path") or
              '/mnt/c/Users/dougl/Documents/Lightshot/')

    list_of_files = glob.glob('{}*'.format(lightshot_path)) # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)

    command = "{} {}".format('/slack upload',latest_file)
    weechat.buffer_set(buf, "input", command)
    weechat.buffer_set(buf, "input_pos", str(len(command)))

    return weechat.WEECHAT_RC_OK


def main():
    if not weechat.register("lightshot", "dzfweb", "1.0.0", "MIT",
                            "Run /slack upload with last lightshot file", "", ""):
        return weechat.WEECHAT_RC_ERROR

    weechat.hook_command("lightshot", "Run /slack upload with last lightshot file", "",
                         "", "", "lightshot", "")

if __name__ == "__main__":
    main()