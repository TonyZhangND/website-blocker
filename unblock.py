import subprocess

TAG = '# Blocked websites'
HOSTS_PATH = '/etc/hosts'


with open(HOSTS_PATH, 'r+') as h:
    lines = h.read().split('\n')

    try:
        i = lines.index(TAG)
        prev_blocked = lines[i+1:]
        lines = lines[:i]

        h.seek(0)
        h.write('\n'.join(lines))
        h.truncate()

        print('These websites are now unblocked:')
        for w in prev_blocked:
            if not w == '':
                print('- %s' %w.split()[1])

    except ValueError:
        print('No websites were blocked')

subprocess.call(['dscacheutil', '-flushcache'])
