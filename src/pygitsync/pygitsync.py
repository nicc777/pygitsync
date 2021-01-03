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
parser.add_argument(
    '--verbose',
    '-v',
    action='count',
    default=0,
    dest='verbosity',
    help='Set verbosity level. Add multiple times to add verbosity (up to three times). Specify at least once to get exception trace dumps.'
)
args = parser.parse_args()


DUMP_ERRORS = False
if args.verbosity > 0:
    print('Verbosity level: {}'.format(args.verbosity))
    DUMP_ERRORS = True


def dump_error(trace_str: str):
    if DUMP_ERRORS is True and trace_str is not None:
        print('EXCEPTION: {}'.format(trace_str))


def create_repo_obj(path: str)->Repo:
    try:
        return Repo(os.path.join(path))
    except:
        dump_error(trace_str=traceback.format_exc())
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

