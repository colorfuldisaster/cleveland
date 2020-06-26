from cleveland.bot import client

import argparse


def start_client(token):
    client.run(token)


def parse_args():
    parser = argparse.ArgumentParser(description='launch cleveland, a bot for the battleship game')
    parser.add_argument('token', help='discord bot authentication token')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    start_client(args.token)


if __name__ == '__main__':
    main()

