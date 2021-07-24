
from shutil import which
import subprocess
from subprocess import DEVNULL, PIPE
def dialog_info(title, text_busy, ok_label):
    title = _(title)
    text_busy = _(text_busy)
    ok_label = _(ok_label)
    if which('zenity'):
        dialog_app = which('zenity')
    elif which('yad'):
        dialog_app = which('yad')
    else:
        dialog_app = None

    if dialog_app is not None:
        messagebox = subprocess.Popen([dialog_app,
                                '--error',
                                '--title=' + title,
                                "--text=" + text_busy,
                                "--ok-label=" + ok_label,
                                '--width=400',
                                '--window-icon=error',
                                '--timeout=50'])
        return 1
