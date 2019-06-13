import json
import random
class IVerbs:
    def guess(self):
        print '# List irregulars verbs #'
        with open('verbs.json') as json_file:
            verbs = json.load(json_file)
        totalVerbs = len(verbs) - 1
        continues = 1
        while(continues):
            start = 0
            verbRandom = random.randint(0, totalVerbs)
            for verb in verbs:
                if verbRandom == start:
                    print "\nVerb:", str(verb)
                    inputPast = raw_input('Past: ')
                    if (verbs[verb]['past'] == inputPast):
                        print '\033[92m ok\033[0m'
                    else:    
                        print '\033[91m x\033[0m'
                    pass
                    inputPastParticiple = raw_input('Past Participles: ')
                    if (verbs[verb]['participles'] == inputPastParticiple):
                        print '\033[92m ok\033[0m'
                    else:    
                        print '\033[91m x\033[0m'
                    pass
                    print 'Verb: %s %s %s %s' % (verb, verbs[verb]['past'], verbs[verb]['participles'], verbs[verb]['translation'])
                    print 'https://www.wordreference.com/es/translation.asp?tranword=%s' % (verb.strip())
                start = start + 1
                pass
            # v = raw_input('Continue y or n: ')
            # if v == 'n':
            #     continues = 0
            #     pass
        print 'This\' the end'
Verb = IVerbs()
Verb.guess()
