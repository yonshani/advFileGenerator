from config.file_suffix_enum import FileSuffixEnum, FileSuffixHandler
from utils.decorators import log_function_status
from utils.tools import Tools


class BaseScenarios:
    def __init__(self):
        # Initialize tools for file handling and read JSON data from the specified file path containing secret information.
        self.tools = Tools()
        self.__data = self.tools.read_json_file(r"config\secrets.json")
        # Retrieve the list of file suffixes to consider for different file types.
        self.suffix_list = FileSuffixHandler().return_enum_list

    @log_function_status
    def generate_all_single_examples_txt_lower_files(self):
        # Generate text files for each secret with lowercase '.txt' extension.
        for secret in self.__data:
            # Create a file name using the secret's name and the '.txt' extension.
            file_name = secret["name"] + FileSuffixEnum.lowercase_text.suffix
            # Create the file with the example text from the secret.
            self.tools.create_file_with_text(file_name=file_name, text=secret["example"])

    @log_function_status
    def generate_ten_single_examples_txt_upper_files(self):
        # Generate text files for each secret with lowercase '.txt' extension.
        for index,secret in enumerate(self.__data):
            if index == 10: return  # Stop after generating five examples.
            # Create a file name using the secret's name and the '.txt' extension.
            file_name = secret["name"] + FileSuffixEnum.uppercase_text.suffix
            # Create the file with the example text from the secret.
            self.tools.create_file_with_text(file_name=file_name, text=secret["example"])

    @log_function_status
    def generate_five_single_examples(self):
        # Generate five single example files using various suffixes.
        for index, secret in enumerate(self.__data):
            if index == 4: return  # Stop after generating five examples.
            for suffix in self.suffix_list:
                # Generate secret text based on the current suffix and secret object.
                secret_text = self.tools.generate_secret_text(suffix=suffix, secret_obj=secret)
                # Create a file name using the secret's name and the appropriate suffix.
                file_name = secret["name"] + suffix
                # Write data to file based on the suffix type.
                if "json" in suffix:
                    self.tools.create_json_file_windows(data=secret_text, file_name=file_name)
                elif "csv" in suffix:
                    self.tools.create_csv_file_windows(data=secret_text, file_name=file_name)
                else:
                    self.tools.create_file_with_text(file_name=file_name, text=secret_text)

    @log_function_status
    def generate_numeric_name_files(self):
        # Generate files with numeric names based on the index.
        for index, secret in enumerate(self.__data):
            if index == 1: return  # Limit to the first two files.
            for suffix in self.suffix_list:
                secret_text = self.tools.generate_secret_text(suffix=suffix, secret_obj=secret)
                # Create a file name using the numeric index and the appropriate suffix.
                file_name = f"{str(index)} + {suffix}"
                # Write data to file based on the suffix type.
                if "json" in suffix:
                    self.tools.create_json_file_windows(data=secret_text, file_name=file_name)
                elif "csv" in suffix:
                    self.tools.create_csv_file_windows(data=secret_text, file_name=file_name)
                else:
                    self.tools.create_file_with_text(file_name=file_name, text=secret_text)

    @log_function_status
    def generate_hebrew_letters(self):
        """Generate text files using Hebrew names; first three as '.txt', the rest as '.TXT'."""
        heb_name = "יונתן"  # Example Hebrew name.
        for index, secret in enumerate(self.__data):
            if index == 4: return  # Limit to the first four files.
            for suffix in self.suffix_list:
                secret_text = self.tools.generate_secret_text(suffix=suffix, secret_obj=secret)
                # Create a file name using the Hebrew name and the appropriate suffix.
                file_name = heb_name + suffix
                # Write data to file based on the suffix type.
                if "json" in suffix:
                    self.tools.create_json_file_windows(data=secret_text, file_name=file_name)
                elif "csv" in suffix:
                    self.tools.create_csv_file_windows(data=secret_text, file_name=file_name)
                else:
                    self.tools.create_file_with_text(file_name=file_name, text=secret_text)

    @log_function_status
    def generate_special_chars_single_examples(self):
        # Generate text files using special character names.
        special_char_list = [
            r"!@#$%^^&()", r"asdasd!@#!@#!", r"asdad@!#^&&(asdad",
            r"adsas.asda.!@#!@.sad", r"🍕!@#asd@!#", r"🌍"
        ]
        for index, secret in enumerate(self.__data):
            if index == 6: return  # Limit to the first six files.
            for suffix in self.suffix_list:
                secret_text = self.tools.generate_secret_text(suffix=suffix, secret_obj=secret)
                # Create a file name using the special character from the list and the appropriate suffix.
                file_name = special_char_list[index] + suffix
                # Write data to file based on the suffix type.
                if "json" in suffix:
                    self.tools.create_json_file_windows(data=secret_text, file_name=file_name)
                elif "csv" in suffix:
                    self.tools.create_csv_file_windows(data=secret_text, file_name=file_name)
                else:
                    self.tools.create_file_with_text(file_name=file_name, text=secret_text)

    @log_function_status
    def recycle_bin_different_files(self):
        """Generate text files with names meant for a recycle bin scenario."""
        recycle_bin_list = [
            r"!@#$%^^&()", r"יותם", r"lorem_ipsum",
            r"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor",
            r"Loremipsumdolorsitamet,consecteturadipiscingelit.Phasellusimperdiet,nullaetdictuminterdum,nisiloremegestaodio,vitaesceleriqueenimligulavenenatisdolor",
            r"."
        ]
        # Create a reverse generator for recycling bin file names.
        generator = self.tools.reverse_generator(recycle_bin_list)
        for index, secret in enumerate(self.__data):
            if index == len(recycle_bin_list) - 1: return  # Limit to the length of recycle bin list.
            gen_data = next(generator)  # Get the next name from the generator.
            for suffix in self.suffix_list:
                secret_text = self.tools.generate_secret_text(suffix=suffix, secret_obj=secret)
                # Create a file name using the generated name and the appropriate suffix.
                file_name = gen_data + suffix
                # Write data to file based on the suffix type.
                if "json" in suffix:
                    self.tools.create_json_file_windows(data=secret_text, file_name=file_name, recycle_bin=True)
                elif "csv" in suffix:
                    self.tools.create_csv_file_windows(data=secret_text, file_name=file_name, recycle_bin=True)
                else:
                    self.tools.create_file_with_text(file_name=file_name, text=secret_text, recycle_bin=True)

    @log_function_status
    def generate_hidden_files_windows(self):
        # Generate hidden files on Windows using secret data.
        for index, secret in enumerate(self.__data):
            if index == 1: return  # Limit to the length of recycle bin list.

            for suffix in self.suffix_list:
                secret_text = self.tools.generate_secret_text(suffix=suffix, secret_obj=secret)
                # Create a file name using the generated name and the appropriate suffix.
                file_name = secret["name"] + suffix
                # Write data to file based on the suffix type.
                if "json" in suffix:
                    self.tools.create_json_file_windows(data=secret_text, file_name=file_name,is_hidden=True)
                elif "csv" in suffix:
                    self.tools.create_csv_file_windows(data=secret_text, file_name=file_name,is_hidden=True)
                else:
                    self.tools.create_hidden_file_windows(file_name=file_name, text=secret_text)

    @log_function_status
    def generate_hidden_files_windows_to_recycle_bin(self):
        # Generate hidden files on Windows using secret data.
        for index, secret in enumerate(self.__data):
            if index == 1: return  # Limit to the length of recycle bin list.

            for suffix in self.suffix_list:
                secret_text = self.tools.generate_secret_text(suffix=suffix, secret_obj=secret)
                # Create a file name using the generated name and the appropriate suffix.
                file_name = secret["name"] + suffix
                # Write data to file based on the suffix type.
                if "json" in suffix:
                    self.tools.create_json_file_windows(data=secret_text, file_name=file_name, recycle_bin=True,is_hidden=True)
                elif "csv" in suffix:
                    self.tools.create_csv_file_windows(data=secret_text, file_name=file_name, recycle_bin=True, is_hidden=True)
                else:
                    self.tools.create_hidden_file_windows(file_name=file_name, text=secret_text,recycle_bin=True)


    @log_function_status
    def generate_file_with_secret_in_mid_text_spaces(self):
        # Generate text file with secret in mid-text with spaces
        for index,secret in enumerate(self.__data):
            if index==1:return
            # Create a file name using the secret's name and the '.txt' extension.
            file_name = secret["name"] + FileSuffixEnum.lowercase_text.suffix
            secret_text = f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco {secret['example']} laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            # Create the file with the example text from the secret.
            self.tools.create_file_with_text(file_name=file_name, text=secret_text)

    @log_function_status
    def generate_file_with_secret_in_mid_text_no_spaces(self):
        # Generate text file with secret in mid-text without spaces
        for index,secret in enumerate(self.__data):
            if index==1:return
            # Create a file name using the secret's name and the '.txt' extension.
            file_name = secret["name"] + FileSuffixEnum.lowercase_text.suffix
            secret_text = f"ipexeacommodoconsequat.Duisauteiruredolorinreprehenderitinvoluptatevelitessecillumdoloreeufugiatnullapariatur.Excepteur sintoccaecatcupidatatnonproident,suntinculpaquiofficiadeseruntmollitanimidestlabor{secret['example']}Loremipsumdolorsitamet,consecteturadipiscingelit.Seddoeiusmodtemporincididuntutlaboreetdoloremagnaaliqua.Utenimadminimveniam,quisnostrudexercitationullamcolaborisnisiutaliq"
            # Create the file with the example text from the secret.
            self.tools.create_file_with_text(file_name=file_name, text=secret_text)

    @log_function_status
    def several_secrets_in_one_file(self):
        secrets = ""
        secret_objs = {}
        for index, secret in enumerate(self.__data):
            if index ==5: break
            secrets +=secret["example"]
            secret_objs[index] = secret


        for suffix in self.suffix_list:
            secret_text = self.tools.generate_secret_text_formatted(suffix=suffix, secrets=secrets)
            file_name = suffix[1:] + suffix
            # Write data to file based on the suffix type.
            if "json" in suffix:
                pass
            elif "csv" in suffix:
                pass
            else:
                self.tools.create_file_with_text(file_name=file_name, text=secret_text)


    @log_function_status
    def generate_hidden_files_nested_dir(self):
        folder_path = "generated_files\\dir1\\dir2\\dir3\\dir4\\dir5\\dir6\\dir7\\dir8\\dir9\\dir10\\"
        # Generate hidden files on Windows using secret data.
        for index, secret in enumerate(self.__data):
            if index == 1: return  # Limit to the length of recycle bin list.

            for suffix in self.suffix_list:
                secret_text = self.tools.generate_secret_text(suffix=suffix, secret_obj=secret)
                # Create a file name using the generated name and the appropriate suffix.
                file_name = secret["name"] + suffix
                # Write data to file based on the suffix type.
                if "json" in suffix:
                    self.tools.create_json_file_windows(folder_path=folder_path,data=secret_text, file_name=file_name, is_hidden=True)
                elif "csv" in suffix:
                    self.tools.create_csv_file_windows(folder_path=folder_path,data=secret_text, file_name=file_name, is_hidden=True)
                else:
                    self.tools.create_hidden_file_windows(folder_path=folder_path,file_name=file_name, text=secret_text)

    @log_function_status
    def generate_single_examples_nested_dir(self):
        folder_path = "generated_files\\dir1\\dir2\\dir3\\dir4\\dir5\\dir6\\dir7\\dir8\\dir9\\dir10\\"
        # Generate five single example files using various suffixes.
        for index, secret in enumerate(self.__data):
            if index == 1: return
            for suffix in self.suffix_list:
                # Generate secret text based on the current suffix and secret object.
                secret_text = self.tools.generate_secret_text(suffix=suffix, secret_obj=secret)
                # Create a file name using the secret's name and the appropriate suffix.
                file_name = secret["name"] + suffix
                # Write data to file based on the suffix type.
                if "json" in suffix:
                    self.tools.create_json_file_windows(folder_path=folder_path,data=secret_text, file_name=file_name)
                elif "csv" in suffix:
                    self.tools.create_csv_file_windows(folder_path=folder_path,data=secret_text, file_name=file_name)
                else:
                    self.tools.create_file_with_text(folder_path=folder_path,file_name=file_name, text=secret_text)

    @log_function_status
    def run_scenarios(self):
        # Execute the scenarios, starting with generating recycle bin files.
        self.generate_single_examples_nested_dir()


