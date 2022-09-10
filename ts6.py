import argparse
from pathlib import Path
import dateparser
from tabulate import tabulate

def starter(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--files")
    parser.add_argument("-d", "--driver")
    p = parser.parse_args(args)
    return check(p)

def timecr(lines,lines2,la,args):
    lines.sort()
    lines2.sort()
    la.sort()
    lines = [i[3:] for i in lines]
    lines2 =[i[3:] for i in lines2]
    c = list(zip(lines,lines2))
    tc = [str(abs(dateparser.parse(i[0])-dateparser.parse(i[1]))) for i in c]
    build_time(tc,la,args)

def build_time(tc,la,args):
    la = [i[4:] for i in la]
    final = dict(zip(la,tc))
    print_time(final,args)

def print_time(fin,args):
    columns = ["Name and Team","Time"]
    sorted_tuple = sorted(fin.items(), key=lambda x: x[1])
    if args.driver:
        for i in sorted_tuple:
            if args.driver in i[0]:
                print(*i)
    else:
        print(tabulate(sorted_tuple,columns,tablefmt='pipe',showindex="always"))

def check(args):
    if args.files:
        filename = "start.log"
        lines = Path(args.files,filename).read_text().splitlines()
        filename = "end.log"
        lines2 = Path(args.files,filename).read_text().splitlines()
        filename = "abbreviations.txt"
        la = Path(args.files,filename).read_text().splitlines()
        timecr(lines,lines2,la,args)
    else:
        return "Error argument"

starter(input().split())