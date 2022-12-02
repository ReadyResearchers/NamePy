# TODO: Add module docstring
"""Add docstring here"""

import re
import json
import libcst as cst
import spacy

# TODO: Create test cases
# TODO: Handle directories
# TODO: Make exit code 1 for failures
# TODO: Make flag to ignore line
# TODO: Dump jsons into new file(s)

NLP = spacy.load("en_core_web_sm")


class IdentifierVisitor(cst.CSTVisitor):
    """Locate identifier nodes and their line and column numbers."""

    METADATA_DEPENDENCIES = (
        cst.metadata.PositionProvider,
        cst.metadata.ParentNodeProvider,
    )

    def __init__(self, current_file_path: str) -> None:
        super().__init__()
        self.current_file_path = current_file_path
        self.identifier_frequency = {
            "Assign": 0,
            "FunctionDef": 0,
            "ClassDef": 0,
            "Parameter": 0,
        }
        self.possible_issues = {
            "Assign": 0,
            "FunctionDef": 0,
            "ClassDef": 0,
            "Parameter": 0,
        }
        self.issue_frequency = {
            "Assign_Too_Long": 0,
            "Assign_Too_Short": 0,
            "Assign_No_Noun": 0,
            "Function_Too_Long": 0,
            "Function_Too_Short": 0,
            "Function_No_Verb": 0,
            "Class_Too_Long": 0,
            "Class_Too_Short": 0,
            "Class_No_Noun": 0,
            "Param_Too_Long": 0,
            "Param_Too_Short": 0,
            "Param_No_Noun": 0,
        }

    def visit_Assign(self, node: cst.Assign) -> None:
        parent = self.get_metadata(cst.metadata.ParentNodeProvider, node)
        for target in node.targets:
            lookup = target.target.value
            pos = self.get_metadata(cst.metadata.PositionProvider, target.target).start
            line_num = pos.line
            column = pos.column
            self.identifier_frequency[("Assign")] +=1
            self.possible_issues[('Assign')] += 3
            # !look = target.target.value if str else blah blah
            if lookup and lookup == str:
                if (len(lookup)) >= 31:
                    print(
                        f"{self.current_file_path}:{line_num}:{column}: Variable '{lookup}' "
                        f"is of length {len(lookup)} -- Consider reducing length."
                    )
                    self.issue_frequency[("Assign_Too_Long")] += 1
                if (len(lookup)) <= 3:
                    if parent.leading_lines and parent.leading_lines[-1].comment:
                        leading_comment = parent.leading_lines[-1].comment.value
                        if leading_comment and lookup in leading_comment:
                            return
                    else:
                        print(
                            f"{self.current_file_path}:{line_num}:{column}: Variable '{lookup}' "
                            f"is of length {len(lookup)} -- Add a comment or increase length."
                        )
                        self.issue_frequency[("Assign_Too_Short")] += 1

                # *Python variables need to be in snake_case
                # Split identifiers by their underscores
                if '_' in lookup:
                    split_name_list = re.split("_+", lookup)
                # Search for noun POS in list
                # Throw error if no noun is found
                    found_noun = False
                    for name in split_name_list:
                        parsed_text = NLP(name)
                        for token in parsed_text:
                            if token.pos_ == "NOUN":
                                found_noun = True
                                break
                            break
                    if not found_noun:
                        print(
                            f"{self.current_file_path}:{line_num}:{column}: Error with variable '{lookup}'"
                            f"-- Consider using a noun."
                        )
                        self.issue_frequency[("Assign_No_Noun")] += 1

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        function_docstring = node.get_docstring()
        lookup = node.name.value
        pos = self.get_metadata(cst.metadata.PositionProvider, node.name).start
        line_num = pos.line
        column = pos.column
        self.identifier_frequency[("FunctionDef")] +=1
        self.possible_issues[('FunctionDef')] += 3
        if (len(lookup)) >= 31:
            print(
                f"{self.current_file_path}:{line_num}:{column}: Function '{lookup}' "
                f"is of length {len(lookup)} -- Consider reducing length."
            )
            self.issue_frequency[("Function_Too_Long")] += 1
        if (len(lookup)) <= 3:
            if function_docstring and lookup in function_docstring:
                return
            else:
                print(
                    f"{self.current_file_path}:{line_num}:{column}: Function '{lookup}' "
                    f"is of length {len(lookup)} -- Add a comment or increase length."
                )
                self.issue_frequency[("Function_Too_Short")] += 1
        # *Python functions need to be in snake_case
        # Split identifiers by their underscores
        split_name_list = re.split("_+", lookup)
        # Search for verb POS in list
        # Throw error if no verb is found
        found_verb = False
        for name in split_name_list:
            parsed_text = NLP(name)
            for token in parsed_text:
                if token.pos_ == "VERB":
                    found_verb = True
                    break
                break
        if not found_verb:
            print(
                f"{self.current_file_path}:{line_num}:{column}: Error with function '{lookup}' "
                f"-- Consider using a verb."
            )
            self.issue_frequency[("Function_No_Verb")] += 1

    def visit_ClassDef(self, node: cst.ClassDef) -> None:
        class_docstring = node.get_docstring()
        lookup = node.name.value
        pos = self.get_metadata(cst.metadata.PositionProvider, node.name).start
        line_num = pos.line
        column = pos.column
        self.identifier_frequency[("ClassDef")] +=1
        self.possible_issues[('ClassDef')] += 3
        if (len(lookup)) >= 31:
            print(
                f"{self.current_file_path}:{line_num}:{column}: Class '{lookup}' "
                f"is of length {len(lookup)} -- Consider reducing length."
            )
            self.issue_frequency[("Class_Too_Long")] += 1
        if (len(lookup)) <= 3:
            if class_docstring and lookup in class_docstring:
                return
            else:
                print(
                    f"{self.current_file_path}:{line_num}:{column}: Class '{lookup}' "
                    f"is of length {len(lookup)} -- Add a comment or increase length."
                )
                self.issue_frequency[("Class_Too_Short")] += 1
        # *Python classes need to be in PascalCase
        # Split identifiers by their uppercase letters
        split_name_list = re.findall("[A-Z][^A-Z]*", lookup)
        # Search for noun POS in list
        # Throw error if no noun is found
        found_noun = False
        for name in split_name_list:
            parsed_text = NLP(name)
            for token in parsed_text:
                if token.pos_ == "NOUN":
                    found_noun = True
                    break
                break
        if not found_noun:
            print(
                f"{self.current_file_path}:{line_num}:{column}: Error with class '{lookup}' "
                f"-- Consider using a noun."
            )
            self.issue_frequency[("Class_No_Noun")] += 1

    def visit_Parameters(self, node: cst.Parameters) -> None:
        parent = self.get_metadata(cst.metadata.ParentNodeProvider, node)
        try:
            parameter_docstring = parent.get_docstring()
        except(AttributeError):
            return
        for param in node.params:
            lookup = param.name.value
            pos = self.get_metadata(cst.metadata.PositionProvider, param).start
            line_num = pos.line
            column = pos.column
            self.identifier_frequency[("Parameter")] +=1
            self.possible_issues[('Parameter')] += 3
            if (len(lookup)) >= 31:
                print(
                    f"{self.current_file_path}:{line_num}:{column}: Parameter '{lookup}' "
                    f"is of length {len(lookup)} -- Consider reducing length."
                )
                self.issue_frequency[("Param_Too_Long")] += 1
            if (len(lookup)) <= 3:
                if parameter_docstring and lookup in parameter_docstring:
                    return
                else:
                    print(
                        f"{self.current_file_path}:{line_num}:{column}: Parameter '{lookup}' "
                        f"is of length {len(lookup)} -- Add a comment or increase length."
                    )
                    self.issue_frequency[("Param_Too_Short")] += 1
            # *Python parameters need to be in snake_case
            # Split identifiers by their underscores
            split_name_list = re.split("_+", lookup)
            # Search for noun POS in list
            # Throw error if no noun is found
            found_noun = False
            for name in split_name_list:
                parsed_text = NLP(name)
                for token in parsed_text:
                    if token.pos_ == "NOUN":
                        found_noun = True
                        break
                    break
            if not found_noun:
                print(
                    f"{self.current_file_path}:{line_num}:{column}: Error with parameter '{lookup}' "
                    f"-- Consider using a noun."
                )
                self.issue_frequency[("Param_No_Noun")] += 1


FILE_PATH = "test_files/basic_files/test_file.py"
# FILE_PATH = "namepy/visitor.py"
# FILE_PATH = "test_files/gatorgrader_files/arguments.py"
with open(FILE_PATH, "r", encoding="utf-8") as infile:
    data = infile.read()
wrapper = cst.metadata.MetadataWrapper(cst.parse_module(data))
# print((cst.parse_module(data)))
my_visitor = IdentifierVisitor(FILE_PATH)
result = wrapper.visit(my_visitor)
# Dump report dictionaries to jsons
issue_report = json.dumps(my_visitor.issue_frequency, indent=4)
identifier_report = json.dumps(my_visitor.identifier_frequency, indent=4)
possible_issue_report = json.dumps(my_visitor.possible_issues, indent=4)
# Find sum of report dictionary values
issue_sum = sum(my_visitor.issue_frequency.values())
identifier_sum = sum(my_visitor.identifier_frequency.values())
possible_issue_sum = sum(my_visitor.possible_issues.values())
# Calculate score out of 10
possible_issue_quotient = possible_issue_sum / 10
error_amount = issue_sum / possible_issue_quotient
correct_amount = 10 - error_amount
FORMAT_FLOAT = "{:.2f}".format(correct_amount)
print(f"\nYour code has been rated a {FORMAT_FLOAT}/10.00\n")
