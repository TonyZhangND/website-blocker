import subprocess

TAG = '# Blocked websites'
HOSTS_PATH = '/etc/hosts'

websites_to_block = ['www.facebook.com', 'facebook.com', 
                    'www.youtube.com', 'youtube.com'
                    ]


with open(HOSTS_PATH, 'r+') as h:
    lines = h.read().split('\n')

    try:
        i = lines.index(TAG)
        already_blocked = lines[i+1:]
        lines = lines[:i+1]
        print('These websites were already being blocked:')
        for w in already_blocked:
            if not w == '':
                print('- %s' %w)
        print('')
        print('Updating list of blocked websites')

    except ValueError:
        lines.append(TAG)
        print('No websites were previously blocked')
        print('')
    
    for w in websites_to_block:
        lines.append('127.0.0.1 %s' %w)
    h.seek(0)
    h.write('\n'.join(lines))
    h.truncate()

subprocess.call(['dscacheutil', '-flushcache'])


print('These websites are now blocked:')
for w in websites_to_block:
    print('- %s' %w)
