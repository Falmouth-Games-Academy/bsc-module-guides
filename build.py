import pygit2
repo = pygit2.Repository('.')
repo.lookup_reference("HEAD").resolve()
head = repo.head
head_name = head.shorthand

from pathlib2 import Path
import subprocess

directory_list = [d for d in Path('.').glob("[a-z]*[0-9]*") if d.is_dir() ]

for d in directory_list:
    working_directory = str(d) + '/slides'
    for i in range(1):
        subprocess.Popen('pdflatex build.tex -jobname=' + str(head_name) + '-' + str(d) + '-' + 'module-guide', cwd = working_directory).wait()