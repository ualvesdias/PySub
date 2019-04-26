import threading
import argparse as ap
from SubDomainSearch import SubDomainSearch
from colorama import init

init()

parser = ap.ArgumentParser(description="Sub domain brute forcer.")
parser.add_argument('-d', '--domain', help='The domain to be brute forced.', required=True)
parser.add_argument('-f', '--file', help='The file containing the sub domains to test.', required=True)
parser.add_argument('-t', '--threads', default=1, type=int, help='The number of threads to work with. Default is 1')
parser.add_argument('-o', '--output', help='Save the results into two files: subdomains and ip\'s.')
args = parser.parse_args()

search = SubDomainSearch(args.file, args.domain, args.threads)

for _ in range(args.threads):
	threading.Thread(target=search.search).start()

search.workqueue.join()

results = search.domainsfound

print('\n#################################################\n')
print('Found a total of %i sub domains.\n' % (len(results)))

if args.output:
	with open(args.output,'w') as outputfile:
		outputfile.write('sub domain,ip address'+'\n')
		for item in results:
			outputfile.write(item[0]+','+item[1]+'\n')
		print('List of sub domains saved in %s.' % (args.output))
else:
	print('List of sub domains found:\n')
	for item in results:
		print('%s,%s' % (item[0],item[1]))