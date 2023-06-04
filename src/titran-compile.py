import sys
import re

def translate_line(line, indent_level):
    line = line.strip()

    # Translate "GOOD MORNING IMSA" to "def main():"
    if line == "GOOD MORNING IMSA":
        return f"def main():"

    # Translate "HEY IMSA [NAME]:" to "def NAME():"
    match = re.match(r"HEY IMSA \[(\w+)\]:", line)
    if match:
        name = match.group(1)
        return f"def {name}():"

    # Translate "HEY IMSA [(A, B, C...) FROM NAME]:" to "def NAME(A, B, C...):"
    match = re.match(r"HEY IMSA \[(.+?) FROM (\w+)\]:", line)
    if match:
        parameters = match.group(1)
        name = match.group(2)
        return f"def {name}({parameters}):"

    # Translate "{content ready for interior of a print statement}" to "print(content)"
    if line.startswith("{") and line.endswith("}"):
        content = line[1:-1].strip()
        return f"{indent_level * '    '}print({content})"

    # Translate "PARAMETER PLEASE REPORT TO {VALUE}" to "PARAMETER = VALUE"
    match = re.match(r"(\w+) PLEASE REPORT TO {(.*?)}", line)
    if match:
        parameter = match.group(1)
        value = match.group(2)
        return f"{indent_level * '    '}{parameter} = {value}"

    # Translate "PARAMETER PLEASE REPORT TO {"prompt" IMMEDIATELY}" to "PARAMETER = input("prompt")"
    match = re.match(r"(\w+) PLEASE REPORT TO {\"(.*)\" IMMEDIATELY}", line)
    if match:
        parameter = match.group(1)
        prompt = match.group(2)
        return f'{indent_level * "    "}{parameter} = input("{prompt}")'
    
    if line == "ITS GONNA BE LIT!" or line == "THE MAIN BUILDING IS CLOSING":
        return f"{indent_level * '    '}"
    
    # Translate "ANNOUNCEMENT FROM [FUNCTION NAME]" to "function_name()"
    match = re.match(r"ANNOUNCEMENT FROM (\w+)", line)
    if match:
        function_name = match.group(1)
        return f"{indent_level * '    '}{function_name}()"

    # Translate "ANNOUNCEMENT BY (A, B, C...) FROM [FUNCTION NAME]" to "function_name(A, B, C...)"
    match = re.match(r"ANNOUNCEMENT BY (.+?) FROM (\w+)", line)
    if match:
        parameters = match.group(1)
        function_name = match.group(2)
        return f"{indent_level * '    '}{function_name}({parameters})"


    # Return the line as is if no translation rule matches
    return f"{indent_level * '    '}{line}"

def translate_titran(code):
    lines = code.split("\n")
    translated_code = []
    main_function = False
    indent_level = 0

    for line in lines:
        print(line, indent_level)
        translated_line = translate_line(line, indent_level)
        translated_code.append(translated_line)

        if line.strip() == "GOOD MORNING IMSA":
            main_function = True

        # Track the indentation level
        if line.strip().startswith("HEY IMSA") or line.strip().startswith("GOOD MORNING IMSA"):
            indent_level += 1
        if line.strip().startswith("ITS GONNA BE LIT!") or line.strip().startswith("THE MAIN BUILDING"):
            indent_level -= 1

    if main_function:
        translated_code.append("if __name__ == \"__main__\":\n\tmain()")

    return "\n".join(translated_code)

def convert(input_file, output_file='output.py'):
    # Read the input file
    with open(input_file, 'r') as file:
        titran_code = file.read().strip()

    # Translate the Titran code
    python_code = translate_titran(titran_code)

    # Save the translated code to the output file
    with open(output_file, 'w') as file:
        file.write(python_code)

def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        if not file_path.endswith('.imsa'):
            raise ValueError("Invalid file extension. File must end with '.imsa'")
        convert(file_path)

    elif len(sys.argv) == 3:
        file_path = sys.argv[1]
        output_file = sys.argv[2]

        if not file_path.endswith('.imsa'):
            raise ValueError("Invalid file extension. File must end with '.imsa'")
        if not output_file.endswith('.py'):
            print(".py will be appended to file extension automatically")
            output_file += '.py'
        
        convert(file_path, output_file)

    else:
        print("Invalid number of arguments. Please provide either one or two arguments.")
        print("Usage: python script.py <file_path>.imsa [output_file.py]")

if __name__ == "__main__":
    main()