import argparse
import os
import socket
import traceback
from git import Repo
from git import RemoteProgress


CWD = os.getcwd()
HOSTNAME = socket.gethostname()


class MyProgressPrinter(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")


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


def check_host_branch_exists(repo: Repo)->bool:
    try:
        branch_count = 0
        for branch in repo.heads:
            print('\t\tbranch: {} [type={}]'.format(branch, type(branch)))
            branch_count += 1
        print('\t\tFound {} branches'.format(branch_count))
    except:
        dump_error(trace_str=traceback.format_exc())
    return False


# FIXME Fetch bug
# The fetch does not seem to work at this point. This is a show stopper.


def run():
    print('Running from [{}] on host [{}]'.format(CWD, HOSTNAME))
    for path in args.paths:
        print('Current repo directory: {}'.format(path))
        repo = create_repo_obj(path=path)
        if repo:
            origin = None
            if 'origin' in repo.remotes:
                origin = repo.remotes.origin
                print('\tRemote found')
                origin.fetch(progress=MyProgressPrinter())
                print('\tRemote fetch completed')
            else: 
                print('\terror: no remote found - skipping this local repo...')

            if origin is not None:
                #repo.fetch(progress=MyProgressPrinter())
                print('\tChecking if host branch exists... ')
                if check_host_branch_exists(repo=repo) is False:
                    print()
                    print('\tCreating remote host branch')
                print('\tBranch checks completed')
            else:
                print('\tOrigin was not defined. skipping repo...')
        else:
            print('error: path [{}] does not appear to be valid. skipping...'.format(path))

