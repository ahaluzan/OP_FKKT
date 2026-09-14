#!/usr/bin/python3

import sys
import subprocess
from pathlib import Path
import os
import ast

try:
    color = sys.stdout.shell
except AttributeError:
    color = None

BASE_DIR = Path(__file__).parent.resolve()

TEST_DIR = BASE_DIR / "testi"

if (BASE_DIR / "naloge.py").exists():
    LOCAL_MODE = True
    STUDENT_DIR = BASE_DIR
    OUTPUT_DIR = BASE_DIR / "rezultat"
else:
    LOCAL_MODE = False
    STUDENT_DIR = Path("/submission")
    OUTPUT_DIR = Path("/app/output")

if not (STUDENT_DIR / "naloge.py").exists():
    print(f"Missing naloge.py in {STUDENT_DIR}")
    sys.exit(1)

TIMEOUT = 2

def run_tests_for_student(student_folder):
    student_output = OUTPUT_DIR / (student_folder.name if not LOCAL_MODE else "")
    student_output.mkdir(parents=True, exist_ok=True)

    if not LOCAL_MODE:
        print(f"\nRunning tests for {student_folder.name}:")

    test_no = 1
    points = []
    detailed_lines = []

    env = os.environ.copy()
    env['PYTHONPATH'] = str(student_folder) + os.pathsep + env.get('PYTHONPATH', '')

    while (TEST_DIR / f"test_{test_no}.py").exists():
        test_file = TEST_DIR / f"test_{test_no}.py"

        unittest_module_code = ast.parse(open(test_file, encoding='utf-8').read())
        unittest_module_doc = ast.get_docstring(unittest_module_code)

        if unittest_module_doc:
            if color is None:
                print(unittest_module_doc)
            else:
                color.write("\n" + unittest_module_doc + "\n", "BUILTIN") 


        process = subprocess.Popen(
            [sys.executable, str(test_file)],
            cwd=student_folder,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
            universal_newlines=True,
            encoding='utf-8'
        )


        try:
            stdout, stderr = process.communicate(timeout=TIMEOUT)
            timeout_occurred = False
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            stderr += "\nTimeout!"
            timeout_occurred = True

        exit_status = process.wait()

        
        if "SyntaxError" in stderr:
            lines = stderr.strip().split("\n")

            syntax_lines = lines[lines.index([line for line in lines if "naloge.py" in line][0]):]

            for line in syntax_lines:
                if "File" in line and "line" in line:
                    line = line.split(",")[-1]

            if color is None:
                print("\n".join(syntax_lines))
            else:
                for line in syntax_lines:
                    color.write(line + "\n", "COMMENT")
            
            color.write("Izhod iz test.py zaradi sintaktične napake.", "ERROR")
            sys.exit()

        short_note = ""
        long_notice = ""
        if len(stderr) > 0:
            lines = stderr.strip().split("\n")
            short_note = lines[-1].lstrip(" : ")
            search = lines[:-1]
            for line in lines[:-1]:
                if "Error" in line: 
                    number = search.index(line)
                    long_notice = "\n".join(search[number:])
                    break
            
         
        point = 1 if exit_status == 0 and not timeout_occurred else 0
        points.append(str(point))

        detailed_lines.append(f"Test {test_no}: ")
        if exit_status == 0 and not timeout_occurred:
            detailed_lines.append("OK")
        else:

            if stdout.strip():
                detailed_lines.append("STDOUT:\n" + stdout.strip())
            detailed_lines.append("STDERR:\n" + stderr.strip())
        detailed_lines.append("") 

        if exit_status == 0:
            notice = "OK"
            notice_color = "STRING"
        elif len(stderr) > 0:
            sn_color = "CONSOLE"
            
            notice = long_notice
            notice_color = "COMMENT"
        else: 
            notice = stdout.strip()
            notice_color = "COMMENT"
            
        message = f"Test {test_no}: {notice}"
        if color is None:
            print(message)
        else:

            color.write(f"Test {test_no}: ", "CONSOLE") 
            if short_note:
                color.write(short_note + "\n", sn_color)
            color.write(notice + "\n", notice_color)
            
        test_no += 1


    with open(student_output / "points.txt", 'w', encoding='utf-8') as f:
        f.write("\n".join(points))

    with open(student_output / "detailed.txt", 'w', encoding='utf-8') as f:
        f.write("\n".join(detailed_lines))

    povzetek = f"\nTests passed: {sum([int(x) for x in points])}/{len(points)}"
    trenutna_ocena = f"\nCurrent grade: {round((sum([int(x) for x in points])/len(points))*100,0) if len(points)!= 0 else 0}"
    if color == None:
        print(povzetek)
        print(trenutna_ocena)
    else:
        color.write(povzetek, "BUILTIN")
        color.write(trenutna_ocena, "BUILTIN")

run_tests_for_student(STUDENT_DIR)
