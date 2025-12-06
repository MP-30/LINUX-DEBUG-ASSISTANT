import argparse
from lda.summary import full_summary
# from lda.llm import llm_debug

parser = argparse.ArgumentParser()
parser.add_argument("command", choices=["summary", "debug"])

args = parser.parse_args()

if args.command == 'summary':
    print(full_summary())
    
# elif args.command == "debug":
#     summary = full_summary()
#     print(llm_debug(summary))