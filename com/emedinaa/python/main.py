#https://docs.python.org/3/library/__main__.html
import argparse

#https://docs.python.org/3/library/argparse.html?highlight=arguments

def getArguments():
    parser = argparse.ArgumentParser(
       description="python arguments" 
    )
    parser.add_argument('--verbose',
                        action= 'store_true',
                        help= 'help parameter')
    return parser.parse_args()

if __name__ == '__main__':
    print('Hello from python')
    args = getArguments()
    print('args:', args)
    argsVerbose = args.verbose
    print('argsVerbose:',argsVerbose)
    print('------------------')


'''
[Running] python3 -u "/Users/eduardo.alfaro/Documents/Bitrise/bitrise-samples/com/emedinaa/python/main.py"
Hello from python
args Namespace(verbose=False)
argsVerbose False 
'''

'''
bitrise-samples % python3 -u "/Users/eduardo.alfaro/Documents/Bitrise/bitrise-samples/com/emedinaa/python/main.py" --verbose
Hello from python
args Namespace(verbose=True)
argsVerbose True
'''
