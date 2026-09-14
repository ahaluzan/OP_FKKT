#!/usr/bin/python3

import sys
import subprocess
from pathlib import Path
import os
import ast
import json
import shutil 

try:
    color = sys.stdout.shell
except AttributeError:
    color = None

USE_DOCKER = os.environ.get("USE_DOCKER") == "1"

BASE_DIR = Path(__file__).parent.resolve()

CONFIG_FILE = BASE_DIR / "config.json"


if USE_DOCKER:
    LOCAL_MODE = False
    DIRS = {
        "testi_dir": "testi",
        "oddano_dir": "/submission",
        "rezultati_dir": "/app/output",
        "filename": "naloge.py"
    }
    STUDENT_DIR = Path(DIRS["oddano_dir"])
    OUTPUT_DIR = Path(DIRS["rezultati_dir"])
    TEST_DIR = BASE_DIR / DIRS["testi_dir"]
    FILENAME = DIRS["filename"]
    DATA_DIR = BASE_DIR / "data"

    # use /tmp for writable temp folder
    TMP_FOLDER_BASE = Path("/tmp/tmp_student")
    TMP_FOLDER_BASE.mkdir(parents=True, exist_ok=True)

elif CONFIG_FILE.exists(): #gabrielle mode
    with open(CONFIG_FILE, "r", encoding="utf8") as f:
        DIRS = json.load(f)

    LOCAL_MODE = False
    OUTPUT_DIR = BASE_DIR / DIRS["rezultati_dir"]
    STUDENT_DIR = BASE_DIR / DIRS["oddano_dir"]
    TEST_DIR = BASE_DIR / DIRS["testi_dir"]
    FILENAME = DIRS.get("filename", "naloge.py")
    DATA_DIR = BASE_DIR / "data"

    
else: # princess
    DIRS = {
    "testi_dir": "testi",
    "oddano_dir": ".",
    "rezultati_dir": "rezultat",
    "filename": "naloge.py",
    }

    #if (BASE_DIR / DIRS["filename"]).exists():
    LOCAL_MODE = True
    STUDENT_DIR = BASE_DIR / DIRS["oddano_dir"]
    OUTPUT_DIR = BASE_DIR / DIRS["rezultati_dir"]
    TEST_DIR = BASE_DIR / DIRS["testi_dir"]
    FILENAME = DIRS["filename"]
    DATA_DIR = BASE_DIR / "data"  # optional

#TEST_DIR = BASE_DIR / DIRS["testi_dir"]

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TIMEOUT = 2

def run_tests_for_student(student_folder, show=True):

    global DATA_DIR

    student_data_dir = None

    env = os.environ.copy()

    if USE_DOCKER and DATA_DIR is not None and DATA_DIR.exists():
        TMP_FOLDER = TMP_FOLDER_BASE / student_folder.name
        shutil.rmtree(TMP_FOLDER, ignore_errors=True)
        shutil.copytree(student_folder, TMP_FOLDER)

        if DATA_DIR is not None and DATA_DIR.exists():
            shutil.copytree(DATA_DIR, TMP_FOLDER / "data")
        
        student_folder = TMP_FOLDER
   
    env['PYTHONPATH'] = str(student_folder) + os.pathsep + env.get('PYTHONPATH', '')

    student_output = OUTPUT_DIR / (student_folder.name if not LOCAL_MODE else "")
    student_output.mkdir(parents=True, exist_ok=True)

    if not LOCAL_MODE and not USE_DOCKER:
        print(f"\nTesting {student_folder.name}:")
        DATA_DIR = BASE_DIR / "data"
        student_data_dir = student_folder / "data"
        if DATA_DIR.exists() and not USE_DOCKER:
            if student_data_dir.exists():
                shutil.rmtree(student_data_dir)
            shutil.copytree(DATA_DIR, student_data_dir)
    
    if not LOCAL_MODE:
        print(f"\nTesting {student_folder.name}:")

    test_no = 1
    points = []
    detailed_lines = []

    while (TEST_DIR / f"test_{test_no}.py").exists():
        test_file = TEST_DIR / f"test_{test_no}.py"

        unittest_module_code = ast.parse(open(test_file, encoding='utf-8').read())
        unittest_module_doc = ast.get_docstring(unittest_module_code)

        if unittest_module_doc:
            if color is None:
                if show:
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

            syntax_lines = []
            for i, line in enumerate(lines):
                if DIRS["filename"] in line:
                    syntax_lines = lines[i:]
                    break

            detailed_lines = ["Syntax Error detected:"] + syntax_lines
            points = ["0"]  

            student_output.mkdir(parents=True, exist_ok=True)
            with open(student_output / "points.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(points))
            with open(student_output / "detailed.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(detailed_lines))

            for line in syntax_lines:
                if "File" in line and "line" in line:
                    line = line.split(",")[-1]

            if color is None:
                if show:
                    print("\n".join(syntax_lines))
                else:
                    print("Sintaktična napaka.")
            else:
                for line in syntax_lines:
                    color.write(line + "\n", "COMMENT")
                color.write("Izhod iz test.py zaradi sintaktične napake.", "ERROR")
            if student_data_dir is not None and student_data_dir.exists():
                shutil.rmtree(student_data_dir)
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
            if show:    
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
        

    if student_data_dir is not None and student_data_dir.exists():
        shutil.rmtree(student_data_dir)

    if USE_DOCKER:
        shutil.rmtree(student_folder, ignore_errors=True)

    vsota = sum([int(x) for x in points])
    povzetek = f"\nTests passed: {vsota}/{len(points)}"
    trenutna_ocena = f"\nCurrent grade: {round((vsota/len(points))*100,0) if len(points)!= 0 else 0}"
    if color == None:
        if show:
            print(povzetek)
            print(trenutna_ocena)
        else:
            print(f"{vsota}/{len(points)}")
            print(f"{round((vsota/len(points))*100,0) if len(points)!= 0 else 0}")

    else:
        color.write(povzetek, "BUILTIN")
        color.write(trenutna_ocena, "BUILTIN")

if USE_DOCKER:
    run_tests_for_student(STUDENT_DIR)
elif LOCAL_MODE:
    run_tests_for_student(STUDENT_DIR)
else:
    for STUDENT in STUDENT_DIR.iterdir():
        if STUDENT.is_dir() and (STUDENT / DIRS["filename"]).exists():
            run_tests_for_student(STUDENT, show=False)