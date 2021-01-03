import argparse
import os
import socket
import traceback
from git import Repo


CWD = os.getcwd()
HOSTNAME = socket.gethostname()


parser = argparse.ArgumentParser(description='Automatically keep a remote git repo and a local directory in sync')
parser.add_argument(
    '--path',
    nargs='*',
    help='One or more local Git repository diretories to auto-sync. By default, the local working directory is used.',
    default=['{}'.format(CWD),],
    dest='paths',
    metavar='PATH'
)
args = parser.parse_args()


def create_repo_obj(path: str)->Repo:
    try:
        return Repo(os.path.join(path))
    except:
        print('EXCEPTION: {}'.format(traceback.format_exc()))
    return None


def run():
    print('Running from [{}] on host [{}]'.format(CWD, HOSTNAME))
    for path in args.paths:
        print('Current repo directory: {}'.format(path))
        repo = create_repo_obj(path=path)
        if repo:
            print('\tChecking if host branch exists... ', end='')
            print('ok')
        else:
            print('error: path [{}] does not appear to be valid. skipping...'.format(path))

