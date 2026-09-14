#!/usr/bin/python3
# natancnejsi testi 25nov25
import subprocess
import sys
import os
import json

def report_fail(out, stdout, abbr_len, color, custom_message):
    #outp = out.strip()[:abbr_len] + (out.strip()[abbr_len:] and '... (string abbreviated)')
    #stdoutp = stdout.strip()[:abbr_len] + (stdout.strip()[abbr_len:] and '... (string abbreviated)')
    outp = out.strip()
    stdoutp = stdout.strip()

        # error message
    if color is None:
        print(custom_message)
    else:
        color.write(custom_message + '\n', "KEYWORD")

    # Found/Expected
    if color is None:
        print('Output doesn\'t match!\nExpected:\n"' + outp + '"\nFound:\n"' + stdoutp + '"')
    else:
        color.write('Output doesn\'t match!\nExpected:\n"', "console")
        color.write(outp, "ERROR")
        color.write('"\nFound:\n"', "console")
        color.write(stdoutp, "ERROR")
        color.write('"' + '\n', "console")


def run_tests(module, to_test, tests_root_dir, test_data, dir_names, default_timeout, abbr_len, is_public):
    tests_root = tests_root_dir+'/'+test_data['rootDir']

    test_no = 1
    tests_passed = 0

    try:
        color = sys.stdout.shell
    except AttributeError:
        color = None

    while True:
        if not os.path.isfile(tests_root+'/'+dir_names['inputDir']+'/test_'+str(test_no)+'.in'):
            break
        
        if len(test_data['timeouts']) >= test_no:
            test_timeout = float(test_data['timeouts'][test_no - 1])
        else:
            test_timeout = default_timeout

        current_env = os.environ.copy()
        current_env['PYTHONIOENCODING']='utf-8'
        process = subprocess.Popen(
            [sys.executable, to_test],
            shell  = False,
            stdin  = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            universal_newlines = True,
            env=current_env,
            encoding = 'utf-8'
        )

        with open(tests_root+'/'+dir_names['inputDir']+'/test_'+str(test_no)+'.in', encoding = 'utf8') as f:
            inpt = f.read()

        with open(tests_root+'/'+dir_names['outputDir']+'/test_'+str(test_no)+'.out', encoding = 'utf8') as f:
            out = f.read()
            # out = pravilne rešitve
            # stdout = kar vrne koda
        try:
            stdout, stderr = process.communicate(inpt, timeout = test_timeout)
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            stdout = stdout[:500]
            if color == None:
                print('Test '+str(test_no)+' timeout!')
            else:
                st = color.write('Test '+str(test_no)+' timeout!'+'\n', "KEYWORD")

        if color == None:
            print('Test '+str(test_no)+':', end=' ')
        else:
            st = color.write('Test '+str(test_no)+': ', "stdin")

        ###################################
        ###### ZACETEK PUBLIC TESTOV ######
        ###################################
        if is_public == True: 
            if test_no == 1:  # preverjanje kategorije A

                #a = "Geslo ni dovolj dolgo. Poskusite ponovno.".count(stdout.strip().replace(" ", "").lower())
                #b = "Geslo ni dovolj dolgo. Poskusite ponovno.".count(out.strip().replace(" ", "").lower())
                
                if len(stderr) > 0:
                    if color == None:
                        print(stderr)
                    else:
                        st = color.write(stderr+'\n',"COMMENT")
                
                elif out.splitlines()[0] in stdout:
                    tests_passed += 1
                    if color == None:
                        print('OK')
                    else:
                        st = color.write('OK\n',"STRING")

                else:
                    report_fail(out, stdout, abbr_len, color, 'Napačna uvrstitev v kategorijo A. Preverite meje in/ali tipkarske napake!')
            
            elif test_no == 2:  # preverjanje uvrščanja v kategorijo B

                if len(stderr) > 0:
                    if color == None:
                        print(stderr)
                    else:
                        st = color.write(stderr+'\n',"COMMENT")
                
                elif out.splitlines()[0] in stdout:
                    tests_passed += 1
                    if color == None:
                        print('OK')
                    else:
                        st = color.write('OK\n',"STRING")

                else:
                    report_fail(out, stdout, abbr_len, color, 'Napačna uvrstitev v kategorijo B. Preverite meje in/ali tipkarske napake!')           
            
            elif test_no == 3: # neveljavna kategorija
                
                if len(stderr) > 0:
                    if color == None:
                        print(stderr)
                    else:
                        st = color.write(stderr+'\n',"COMMENT")
                
                elif out.splitlines()[0] in stdout:
                    tests_passed += 1
                    if color == None:
                        print('OK')
                    else:
                        st = color.write('OK\n',"STRING")

                else:
                    report_fail(out, stdout, abbr_len, color, 'Napačno obravnavanje neveljavne kategorije. Preverite pogoje in/ali tipkarske napake!')
            
            elif test_no == 4: # preverjanje zavrnjene prijave

                a = "Vnesi ime: Vnesi tedensko razdaljo v km: Zavrnjena prijava."
                b = "Napačno obravnavanje zavrnjene prijave. Preverite pogoje in/ali tipkarske napake!\n"

                if len(stderr) > 0:
                    if color == None:
                        print(stderr)
                    else:
                        st = color.write(stderr+'\n',"COMMENT")
                
                elif a in stdout:
                    tests_passed += 1
                    if color == None:
                        print('OK')
                    else:
                        st = color.write('OK\n',"STRING")

                else:
                    report_fail(out, stdout, abbr_len, color, b)

            elif test_no == 5: # razdalja nad 30 in izbor A

                #a = "Vnesi ime: Vnesi tedensko razdaljo v km: Vnesi želeno kategorijo (A, B): Uvrstitev v kategorijo A."
                b = "Neustrezno upoštevanje možnosti izbire kategorije A za tekače, ki presegajo 30 km na teden. Preverite tudi tipkarske napake!\n"

                if len(stderr) > 0:
                    if color == None:
                        print(stderr)
                    else:
                        st = color.write(stderr+'\n',"COMMENT")
                
                elif out.splitlines()[0] in stdout:
                    tests_passed += 1
                    if color == None:
                        print('OK')
                    else:
                        st = color.write('OK\n',"STRING")

                else:
                    report_fail(out, stdout, abbr_len, color, b)

            elif test_no == 6: # razdalja nad 30 in izbor B

                #a = "Vnesi ime: Vnesi tedensko razdaljo v km: Vnesi želeno kategorijo (A, B): Uvrstitev v kategorijo B."
                b = "Neustrezno upoštevanje možnosti izbire kategorije B za tekače, ki presegajo 30 km na teden. Preverite tudi tipkarske napake!\n"

                if len(stderr) > 0:
                    if color == None:
                        print(stderr)
                    else:
                        st = color.write(stderr+'\n',"COMMENT")
                
                elif out.splitlines()[0] in stdout:
                    tests_passed += 1
                    if color == None:
                        print('OK')
                    else:
                        st = color.write('OK\n',"STRING")

                else:
                    report_fail(out, stdout, abbr_len, color, b)

            elif test_no == 7: # izpis števila tekmovalcev 

                #a = "Želite izpis števila tekmovalcev ali seznama tekmovalcev? (s/v): Kategorija A: 3; kategorija B: 2; zavrnjeni: 0"
                b = "Program ne izpisuje števila tekmovalcev v posameznih kategorijah. Preverite tudi tipkarske napake!\n"

                if len(stderr) > 0:
                    if color == None:
                        print(stderr)
                    else:
                        st = color.write(stderr+'\n',"COMMENT")
                
                elif out.splitlines()[11] in stdout:
                    tests_passed += 1
                    if color == None:
                        print('OK')
                    else:
                        st = color.write('OK\n',"STRING")

                else:
                    report_fail(out, stdout, abbr_len, color, b)

            elif test_no == 8: # izpis poimenskega seznama

                #a = "Želite izpis števila tekmovalcev ali seznama tekmovalcev? (s/v): Kategorija A: ['Marjanca', 'Rozalija']; kategorija B: ['Marija', 'Franc']; zavrnjeni: []"
                b = "Program ne izpiše poimenskih seznamov števila tekmovalcev v posameznih kategorijah. Preverite tudi tipkarske napake!\n"

                if len(stderr) > 0:
                    if color == None:
                        print(stderr)
                    else:
                        st = color.write(stderr+'\n',"COMMENT")
                
                elif out.splitlines()[9] in stdout:
                    tests_passed += 1
                    if color == None:
                        print('OK')
                    else:
                        st = color.write('OK\n',"STRING")

                else:
                    report_fail(out, stdout, abbr_len, color, b)
            
            else:
                if len(stderr) > 0:
                    if color == None:
                        print(stderr)
                    else:
                        st = color.write(stderr+'\n',"COMMENT")
                elif stdout.strip().replace(" ", "").lower() == out.strip().replace(" ", "").lower():
                    tests_passed += 1
                    if color == None:
                        print('OK')
                    else:
                        st = color.write('OK\n',"STRING")

                else:
                    report_fail(out, stdout, abbr_len, color, "Napacna izvedba naloge.")
                       

        ###################################
        ##### ZACETEK PRIVATE TESTOV ######
        ###################################
        else:
            if len(stderr) > 0:
                if color == None:
                    print(stderr)
                else:
                    st = color.write(stderr+'\n',"COMMENT")
            elif stdout.strip().replace(" ", "").lower() == out.strip().replace(" ", "").lower():
                tests_passed += 1
                if color == None:
                    print('OK')
                else:
                    st = color.write('OK\n',"STRING")

            else:
                outp = out.strip()[:abbr_len] + (out.strip()[abbr_len:] and '... (string abbreviated, full string in the output directory)')
                stdoutp = stdout.strip()[:abbr_len] + (stdout.strip()[abbr_len:] and '... (string abbreviated, full string in the results directory)') 
                if color == None:
                    print('Output doesn\'t match!\nExpected:\n"'+outp+'"\nFound:\n"'+stdoutp+'"')
                else:
                    st = color.write('Output doesn\'t match!\nExpected:\n"', "console")
                    st = color.write(outp, "ERROR")
                    st = color.write('"\nFound:\n"', "console")
                    st = color.write(stdoutp, "ERROR")
                    st = color.write('"'+'\n', "console")

        if not os.path.exists(tests_root+'/'+dir_names['resultsDir']):
            os.makedirs(tests_root+'/'+dir_names['resultsDir'])
        with open(tests_root+'/'+dir_names['resultsDir']+'/test_'+str(test_no)+'.res', 'w', encoding = 'utf8') as f:
            f.write(stdout)
            
        test_no += 1
    
    print('Tests passed: '+str(tests_passed)+'/'+str(test_no-1))

def main():

    config_file = os.path.dirname(os.path.realpath(__file__))+'/config.json'
    
    #print(f'This is config_file path: {config_file}')
      
    if not os.path.isfile(config_file):
        config_file = 'config.json'
    
    with open(config_file) as json_data:
        data = json.load(json_data)
        #print(f'json data: {data}')
        modules_to_test = data['modulesToTest']

        # debug line
        # print(f'These are modules to test: {modules_to_test}')

        to_test_root_dir = data['toTestRootDir']
        #print(f'To test root dir: {to_test_root_dir}')

        if len(sys.argv) > 1:
            if os.path.isdir(sys.argv[1]):
               to_test_root_dir = sys.argv[1]
        
        for module_data in modules_to_test:
            module = module_data['moduleName']
            to_test = to_test_root_dir +'/'+module+'.py'
            
            # debug line
            #print(f'This is to_test_root_dir: {to_test_root_dir}')
            #print(f'This is to_test: {to_test}')
            
            if 'testsRootDir' not in data: 
                tests_root_dir = os.path.dirname(os.path.realpath(__file__))
            else:
                tests_root_dir = data['testsRootDir']
                
            if os.path.isfile(to_test):
                print('Public tests:')
                run_tests(module_data['moduleName'], to_test, tests_root_dir, module_data['publicTests'], data["testDirNames"], float(data['defaultTimeout']), int(data['abbreviatedOutputLen']), is_public=True)

                #print(f'moduiledata: {module_data}')
                
                if os.path.isdir('private'):
                    print('Private tests:')
                    run_tests(module_data['moduleName'], to_test, tests_root_dir, module_data['privateTests'], data["testDirNames"], float(data['defaultTimeout']), int(data['abbreviatedOutputLen']), is_public=False)

            else:
                # debug
                # print(f'This is module: {module}')

                print('File '+module+'.py missing.')

if __name__ == "__main__":
    main()




