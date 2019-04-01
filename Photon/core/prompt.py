import os
import tempfile

def prompt(default=None):
    editor = 'vim'
    with tempfile.NamedTemporaryFile(mode='r+') as tmpfile:
        if default:
            tmpfile.write(default)
            tmpfile.flush()

        child_pid = os.fork()
        is_child = child_pid == 0
        # Child process
        if is_child:
            os.execvp(editor, [editor, tmpfile.name])
        # Parent process
        else:
            os.waitpid(child_pid, 0) # Wait for child process and kill it
            tmpfile.seek(0) # Move file descriptor to the beginning
            return tmpfile.read().strip()
