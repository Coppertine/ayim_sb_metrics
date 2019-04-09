import os
import progressbar
from shutil import copyfile
from glob import iglob
from osb_file_parser import osz_contains_storyboard


def copy_to_output_folder(files):
    print("Copying all Storyboard OSZ's to Output folder.")
    for f in progressbar.progressbar(files):
        os.makedirs("output\{0}".format(os.path.dirname(f)), exist_ok=True)
        copyfile(f, "output\{0}".format(f))
        
def run_statistics(files):
    replace_variables(files)
    print("Running Statistics on all Storyboards, will take a while")
    for f in progressbar.progressbar(files):
        sprite_count(f)
        command_count(f)
        file_sizes(f)
    
        


if __name__ == '__main__':
    all_osz = list(iglob('maps/**/**/*.osz', recursive=True))
    files = []
    error_log = open("error.log", "w")
    for file_path in progressbar.progressbar(all_osz):
        try:
            if osz_contains_storyboard(file_path):
                files.append(file_path)
        except Exception as error:
            error_log.write(f"ERROR: \n{0}\n{1}\n\n".format(file_path, error))

    copy_to_output_folder(files)
    run_statisitcs(list(iglob('output/**/**/*.osz', recursive=True)))
