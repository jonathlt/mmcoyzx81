import re

def remove_section(input_text, start_string, end_string):
    output = re.sub(f'{start_string}.*?{end_string}', '', input_text, flags=re.DOTALL)
    return output

def main():
    f = open('mmcoyzx81-0.1.9/chapter04.html')
    file_string = f.read()
    output = remove_section(file_string,'<!-- This is the banner vvvv -->','<!-- This is the banner \\^\\^\\^\\^ -->')
    print(output)
    f = open('mmcoyzx81-0.1.9_output/chapter04.html','w')
    output = remove_section(output, '<!-- This is the copyright line vvvv -->','<!-- This is the copyright line \\^\\^\\^\\^ -->')
    output = remove_section(output, '<!-- This is the content navigation vvvv -->','<!-- This is the content navigation \\^\\^\\^\\^ -->')
    output = remove_section(output, '<div class="contentjsforidx">','</div>')
    output = remove_section(output, '<!-- This is the main menu vvvv -->','<!-- This is the main menu \\^\\^\\^\\^ -->')
    output = remove_section(output, '<!-- This is the local menu vvvv -->','<!-- This is the local menu \\^\\^\\^\\^ -->')
    f.write(output)
    f.close()

if __name__ == '__main__':
    main()