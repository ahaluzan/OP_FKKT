#!/usr/bin/python3

import subprocess
import sys
import os
import json
import ast

def run_tests(assignment, to_test, tests_root_dir, test_data, dir_names, default_timeout):
    tests_root = test_data['rootDir']
    test_no = 1
    tests_passed = 0
    while os.path.isfile(tests_root+'/'+dir_names['unitTestDir']+'/'+assignment+'/test_'+str(test_no)+'.py'):
      
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
        unittest_file = tests_root+'/'+dir_names['unitTestDir']+'/'+assignment+'/test_'+str(test_no)
        unittest_module = unittest_file.replace('/', '.')
        
        timeout = False
        try:
            stdout, stderr = process.communicate(unittest_module, timeout = test_timeout)
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            stdout = stdout[:500]
            timeout = True
            
        exit_status = process.wait()
        
        unittest_module_code = ast.parse(open(unittest_file+'.py', encoding = 'utf8').read())
        unittest_module_doc = ast.get_docstring(unittest_module_code)
        
        if unittest_module_doc:
            print(unittest_module_doc) 
            
        print('Test '+str(test_no)+':', end=' ')
        if timeout:  
            stderr += 'Timeout!'
            
        if exit_status == 0:
            tests_passed += 1
            print('OK')
            stderr += 'OK'
        elif len(stderr) > 0:
            print(stderr.strip())
        else:
            print(stdout.strip())
    
        if not os.path.exists(tests_root+'/'+dir_names['unitTestResultsDir']+'/'+assignment):
            os.makedirs(tests_root+'/'+dir_names['unitTestResultsDir']+'/'+assignment)
        with open(tests_root+'/'+dir_names['unitTestResultsDir']+'/'+assignment+'/test_'+str(test_no)+'.txt', 'w', encoding = 'utf8') as f:
            f.write(stderr)

        if not os.path.exists(tests_root+'/'+dir_names['unitTestStdoutDir']+'/'+assignment):
            os.makedirs(tests_root+'/'+dir_names['unitTestStdoutDir']+'/'+assignment)
        with open(tests_root+'/'+dir_names['unitTestStdoutDir']+'/'+assignment+'/test_'+str(test_no)+'.txt', 'w', encoding = 'utf8') as f:
            f.write(stdout)
        
        test_no += 1


    print('Tests passed: '+str(tests_passed)+'/'+str(test_no-1))

def main():

    config_file = os.path.dirname(os.path.realpath(__file__))+'/config.json'
      
    if not os.path.isfile(config_file):
        config_file = 'config.json'
    
    with open(config_file) as json_data:
        data = json.load(json_data)
        assignments_to_test = data['assignmentsToTest']

        for assignment_data in assignments_to_test:
            if 'testsRootDir' not in data: 
                tests_root_dir = os.path.dirname(os.path.realpath(__file__))
            else:
                tests_root_dir = data['testsRootDir']
                
            test_wrapper =  tests_root_dir +'/test_wrapper.py'
            if os.path.isfile(test_wrapper):
                print('Public tests:')
                run_tests(assignment_data['assignmentName'], test_wrapper, tests_root_dir, assignment_data['publicTests'], data["testDirNames"], float(data['defaultTimeout']))
                print('Private tests:')
                run_tests(assignment_data['assignmentName'], test_wrapper, tests_root_dir, assignment_data['privateTests'], data["testDirNames"] , float(data['defaultTimeout']))
            else:
                print('File test_wrapper.py missing.')

if __name__ == "__main__":
    main()


