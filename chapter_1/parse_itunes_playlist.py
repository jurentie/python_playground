#A simple project that finds duplicate music tracks
#in iTunes plalist files and plots various 
#statistics such as track lengths and ratings.


import sys
verbose = False

def findDuplicates(filename):
	if(verbose):
		print('Finding duplicate tracks in %s...' % filename)


def main():
	#Check if there is a single argument after script call
	if(len(sys.argv) == 2):
		#Get argument
		arg1 = sys.argv[1]
		#Set verbose to true to print out information
		if(arg1 == "-v" or arg1 == "--v"
		or arg1 == "--verbose" or arg1 == "-verbose"):
			verbose = True


if __name__ == "__main__":
	main()