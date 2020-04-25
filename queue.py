#!/usr/bin/env python3

import argparse
import sys
import os

def main():
    """ ------------------- argparse -------------------- """
    parser = argparse.ArgumentParser(description="queue of problems", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("command", help=
            "add -- add a problem to the queue\n" +
            "list -- list all problems in the queue\n" +
            "drop -- drop a problem from the queue\n" +
            "done -- mark as completed and drop\n"
    )
    parser.add_argument("option",
            nargs="*", default=None,
            help="id to add/remove"
    )

    args = parser.parse_args()

    if args.command not in ["add", "list", "drop", "done"]:
        print("UNKNOWN COMMAND")
        return

    path = os.path.join(os.path.dirname(__file__), "q.txt")

    q = []
    with open(path, "r") as f:
        for line in f:
            q.append(line)


    if args.command == "list":
        sys.stdout.write("".join(q))
        return

    if args.option is None:
        print("specify problem to add/drop")
        return

    if args.command == "add":
        for it in args.option:
            name = it + "\n"
            if name in q[1:]:
                print("{} is already in the queue".format(name.strip()))
            else:
                q.append(name)
                with open(path, "a") as f:
                    f.write(name)
        sys.stdout.write("".join(q))

    else:
        for it in args.option:
            name = it + "\n"
            if name not in q[1:]:
                print("{} is not in the queue".format(name.strip()))
            else:
                q.remove(name)
                if args.command == "done":
                    num = int(q[0].split()[1])
                    q[0] = "Completed: {}\n".format(num+1)
                with open(path, "w") as f:
                    f.write("".join(q))
        sys.stdout.write("".join(q))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        sys.exit(0)
