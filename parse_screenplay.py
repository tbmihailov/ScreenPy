import json
import sys
import time

from screenpy.screenpile import annotate

if __name__ == '__main__':
	screenplay = 'indianajonesandtheraidersofthelostark.txt'
	if len(sys.argv) > 1:
		screenplay = sys.argv[1]

	screenplay_out_json = 'indianajonesandtheraidersofthelostark.json'
	if len(sys.argv) > 2:
		screenplay_out_json = sys.argv[2]

	print("Processing screenplay {0}".format(screenplay))
	start = time.time()
	with open(screenplay, 'r') as fn:
		play = fn.read()

	masta = annotate(play)
	print("num masta:{0}".format(len(masta)))

	print("done in {0} s".format(time.time() - start))
	with open(screenplay_out_json, 'w') as fp:
		json.dump(masta, fp, indent=4)

	print("Exported to {0}".format(screenplay_out_json))



