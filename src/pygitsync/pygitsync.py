import argparse
import os


cwd = os.getcwd()


parser = argparse.ArgumentParser(description='Automatically keep a remote git repo and a local directory in sync')
parser.add_argument(
    '--path',
    nargs='*',
    help='One or more local Git repository diretories to auto-sync. By default, the local working directory is used.',
    default='{}'.format(cwd),
    action='append'
)
args = parser.parse_args()


def run():
    print('Running from [{}]'.format(cwd))
    print('Local directories: {}'.format(args.path))

