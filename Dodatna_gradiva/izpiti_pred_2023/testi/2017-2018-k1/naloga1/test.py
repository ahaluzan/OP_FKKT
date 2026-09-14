#!/usr/bin/python3

import subprocess
import sys
import os
import json

def run_tests(module, to_test, tests_root_dir, test_data, dir_names, default_timeout):
    tests_root = tests_root_dir+'/'+test_data['rootDir']
    test_no = 1
    tests_passed = 0
    while True:
        if not os.path.isfile(tests_root+'/'+dir_names['inputDir']+'/test_'+str(test_no)+'.in'):
            break
        
        if len(test_data['timeouts']) >= test_no:
            test_timeout = float(test_data['timeouts'][test_no - 1])
        else:
            test_timeout = default_timeout
            
        process = subprocess.Popen(
            [sys.executable, to_test],
            shell  = False,
            stdin  = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            universal_newlines = True
        )

        with open(tests_root+'/'+dir_names['inputDir']+'/test_'+str(test_no)+'.in', encoding = 'utf8') as f:
            inpt = f.read()

        with open(tests_root+'/'+dir_names['outputDir']+'/test_'+str(test_no)+'.out', encoding = 'utf8') as f:
            out = f.read()

        try:
            stdout, stderr = process.communicate(inpt, timeout = test_timeout)
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            stdout = stdout[:500]
            print('Test '+str(test_no)+' timeout!')

        print('Test '+str(test_no)+':', end=' ')
        if len(stderr) > 0:
            print(stderr)
        elif stdout.strip().replace(" ", "").lower() == out.strip().replace(" ", "").lower():
            tests_passed += 1
            print('OK')
        else:
            outp = out.strip()[:92] + (out.strip()[92:] and '... (string abbreviated, full string in the output directory)')
            stdoutp = stdout.strip()[:92] + (stdout.strip()[92:] and '... (string abbreviated, full string in the results directory)') 
            print('Output doesn\'t match: expected "'+outp+'", found "'+stdoutp+'"')
#            print('expected "'+out.strip(),'", found "'+stdout.strip()+'"')

        if not os.path.exists(tests_root+'/'+dir_names['resultsDir']):
            os.makedirs(tests_root+'/'+dir_names['resultsDir'])
        with open(tests_root+'/'+dir_names['resultsDir']+'/test_'+str(test_no)+'.res', 'w', encoding = 'utf8') as f:
            f.write(stdout)
            
        test_no += 1

    print('Tests passed: '+str(tests_passed)+'/'+str(test_no-1))

    #exit_status = process.wait()
    #print(exit_status)

def main():

    config_file = os.path.dirname(os.path.realpath(__file__))+'/config.json'
      
    if not os.path.isfile(config_file):
        config_file = 'config.json'
    
    with open(config_file) as json_data:
        data = json.load(json_data)
        modules_to_test = data['modulesToTest']

        to_test_root_dir = data['toTestRootDir']
        if len(sys.argv) > 1:
            if os.path.isdir(sys.argv[1]):
               to_test_root_dir = sys.argv[1]
        
        for module_data in modules_to_test:
            module = module_data['moduleName']
            to_test = to_test_root_dir +'/'+module+'.py'
            if 'testsRootDir' not in data: 
                tests_root_dir = os.path.dirname(os.path.realpath(__file__))
            else:
                tests_root_dir = data['testsRootDir']
                
            if os.path.isfile(to_test):
                print('Public tests:')
                run_tests(module_data['moduleName'], to_test, tests_root_dir, module_data['publicTests'], data["testDirNames"], float(data['defaultTimeout']))
                print('Private tests:')
                run_tests(module_data['moduleName'], to_test, tests_root_dir, module_data['privateTests'], data["testDirNames"], float(data['defaultTimeout']))

            else:
                print('File '+module+'.py missing.')

if __name__ == "__main__":
    main()




