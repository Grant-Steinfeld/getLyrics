import glob

f=[]
for filename in glob.glob('/Users/grantsteinfeld/Documents/dev/CLIENTS/agentidea/grabSongCoripi/corpi/allCatted/*.txt'):
    f.append( filename )

allFileName = '/Users/grantsteinfeld/Documents/dev/CLIENTS/agentidea/grabSongCoripi/corpi/allSongs.txt'

for ff in f:
    with open(allFileName, 'a') as af:
        with open(ff, 'r') as rf:

            artist = ff.split('/')[-1]

            af.write('[{}]'.format(artist[:-7]))
            af.write('\n\n')
            af.write('{}'.format(rf.read()))
            af.write('\n\n')
            af.write('\n\n')