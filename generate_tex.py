#!/usr/bin/env python
import re
import glob
import subprocess

HEADER_FILE = 'header.tex'
FOOTER_FILE = 'footer.tex'

SECTION_BREAK = ''

CODE_START = r'\begin{minted}{python}'
CODE_END = r'\end{minted}'

class HomeworkProblem(object):
    def __init__(self, number=None, part=None, text_filepath=None, code_filepath=None, input_filepath=None, existing_output_filepath=None):
        self.number = number
        self.part = part
        self.text_filepath = text_filepath
        self.code_filepath = code_filepath
        self.input_filepath = input_filepath
        self.existing_output_filepath = existing_output_filepath

        if self.existing_output_filepath is None:
            self.postrun_output_filepath = self.get_output_filepath()
        else:
            self.postrun_output_filepath = None

    def get_output_filepath(self):
        """
        Returns the place that running the script should put the output
        """
        return 'problem-{number}-{part}.auto_output'.format(number=self.number, part=self.part)

    def generate_latex(self):
        """
        Returns the generated latex for this problem.
        Order:
            number & part
            Text (if exists)
            Code (if exists)
            IF existing_output_filepath:
                existing output
            ELSE:
                IF input_filepath:
                    run with input and store output in postrun_output_filepath
                ELSE:
                    run without input and store output in postrun_output_filepath
        """

        all_lines = []
        text_lines = []
        code_lines = []
        existing_output_lines = []
        postrun_output_lines = []

        if self.text_filepath:
            text_lines = self.get_file_lines(self.text_filepath)
        if self.code_filepath:
            code_lines = self.get_file_lines(self.code_filepath)
        if self.existing_output_filepath:
            existing_output_lines = self.get_file_lines(self.existing_output_filepath)
        else:
            run_command = ['/usr/bin/env', 'python', self.code_filepath]

            output_pipe = open(self.postrun_output_filepath, 'w')
            input_pipe = subprocess.PIPE
            if self.input_filepath:
                input_pipe = open(self.input_filepath, 'r')

            proc = subprocess.Popen(run_command, stdin=input_pipe, stdout=output_pipe)
            _, stderr = proc.communicate()
            # TODO handle stderr

            postrun_output_lines = self.get_file_lines(self.postrun_output_filepath)

        title_string = 'Problem {number}.{part}'.format(number=self.number, part=self.part)

        all_lines.append(title_string)

        if text_lines:
            all_lines.extend(text_lines)
        if code_lines:
            all_lines.append(CODE_START)
            all_lines.extend(code_lines)
            all_lines.append(CODE_END)
        if existing_output_lines:
            all_lines.extend(existing_output_lines)
        if postrun_output_lines:
            all_lines.extend(postrun_output_lines)

        return all_lines

    def get_file_lines(self, filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()
            return lines


def get_problems():
    problem_filename_regex = r'problem-(?P<number>\d+)-(?P<part>.+)\.(?P<fileextension>py|input|txt|output)'
    compiled_regex = re.compile(problem_filename_regex)

    glob_pattern = 'problem-*.*'
    files = glob.glob(glob_pattern)

    problems = {}
    for filename in files:
        match = compiled_regex.search(filename)
        if match is None:
            # TODO output error
            continue
        group_matches = match.groupdict()

        key_str = '{number}-{part}'.format(number=group_matches['number'], part=group_matches['part'])

        if not key_str in problems:
            problems[key_str] = {
                'number': group_matches['number'],
                'part': group_matches['part'],
                'py': None,
                'input': None,
                'txt': None,
                'output': None,
            }

        problems[key_str][group_matches['fileextension']] = filename

    sorted_problem_keys = sorted(problems.keys())

    hw_problems = []
    for key in sorted_problem_keys:
        hw_problem = HomeworkProblem(number=problems[key]['number'],
                part=problems[key]['part'],
                code_filepath=problems[key]['py'],
                input_filepath=problems[key]['input'],
                text_filepath=problems[key]['txt'],
                existing_output_filepath=problems[key]['output']
            )

        hw_problems.append(hw_problem)

    return hw_problems
