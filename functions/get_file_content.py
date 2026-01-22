import os

def get_file_content(working_directory, file_path):
	max_characters  = 10000
	working_dir_abs = os.path.abspath(working_directory)
	target_file     = os.path.normpath(os.path.join(working_dir_abs, file_path))

	try:
		if not os.path.isfile(target_file):
			return f'Error: File not found or is not a regular file: "{file_path}"'

		# Will be True or False
		valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

		if not valid_target_dir:
			return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

		with open(target_file, "r") as f:
			file_content_string = f.read(max_characters)

			if f.read(1):
				file_content_string += f'[...File "{file_path}" truncated at {max_characters} characters]'

			return file_content_string
	except FileNotFoundError:
		return f'Error: {file_path} was not found in the working directory.'
