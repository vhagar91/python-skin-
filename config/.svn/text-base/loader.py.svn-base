
import os
import yaml
import struct
import traceback
from cStringIO import StringIO
from Crypto import Random
from Crypto.Cipher import AES


GSKIN_BASE_PATH = os.getcwd()
GSKIN_CONFIG_PATH = os.path.join(GSKIN_BASE_PATH, 'config', 'config.yml')
GCLIENT_BASE_PATH = yaml.load(open(GSKIN_CONFIG_PATH))['client_url']

if not os.path.exists(GCLIENT_BASE_PATH):
    raise Exception('Cant find gclient installation directory.')

GCLIENT_CONFIG_PATH = os.path.join(GCLIENT_BASE_PATH, 'config', 'config.yml')
GCLIENT_DB_PATH = os.path.join(GCLIENT_BASE_PATH, 'db', 'gclient.db')
__KEY = 'gggggggggggggggggggggggggggggggg'
__BLOCK_SIZE = 64 * 1024


def is_root():
    if os.name == 'nt':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except Exception as e:
            print "Admin check failed, assuming not an admin."
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    else:
        raise RuntimeError("Unsupported operating system for this module: %s" % (os.name,))


def load(in_filename, yml=True, ciphered=False):
    if ciphered:
        data = __decrypt(in_filename).getvalue()
    else:
        data = open(in_filename).read()
    if yml:
        return yaml.load(data)
    return data


def save(data, out_filename, yml=True, ciphered=True):

    if yml:
        data = yaml.dump(data)

    if ciphered:
        __encrypt(StringIO(data), out_filename)
    else:
        outfile = open(out_filename, 'w')
        outfile.write(data)
        outfile.close()


def __encrypt(buff_ent, out_filename):

    IV = Random.new().read(16)
    encryptor = AES.new(__KEY, AES.MODE_CBC, IV)
    buff_size = len(buff_ent.getvalue())
    with open(out_filename, 'wb') as outfile:
        outfile.write(struct.pack('<Q', buff_size))
        outfile.write(IV)

        while True:
            chunk = buff_ent.read(__BLOCK_SIZE)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += ' ' * (16 - len(chunk) % 16)

            outfile.write(encryptor.encrypt(chunk))


def __decrypt(in_filename):

    buff_sal = StringIO()
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        IV = infile.read(16)
        decryptor = AES.new(__KEY, AES.MODE_CBC, IV)

        while True:
            chunk = infile.read(__BLOCK_SIZE)
            if len(chunk) == 0:
                break
            buff_sal.write(decryptor.decrypt(chunk))

        buff_sal.truncate(origsize)
    return buff_sal
