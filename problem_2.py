import os

def find_files(suffix, path):
	"""
	Find all files beneath path with file name suffix.

	Note that a path may contain further subdirectories
	and those subdirectories may also contain further subdirectories.

	There are no limit to the depth of the subdirectories can be.

	Args:
	suffix(str): suffix if the file name to be found
	path(str): path of the file system

	Returns:
	a list of paths
	"""

	files_with_suffix = list()

	for dir_content in os.listdir(path):
		sub_path = os.path.join(path, dir_content)

		if os.path.isfile(sub_path) and dir_content.endswith(suffix):
			files_with_suffix.append(dir_content)

		elif os.path.isdir(sub_path):
			files_with_suffix += find_files(suffix, sub_path)

	return files_with_suffix


''' Test case 1: Root directory '''
print(find_files('.c', 'testdir'))
# Expected output: ['a.c', 'a.c', 't1.c', 'b.c']


''' Test case 2: Sub directory containing .c file '''
print(find_files('.c', 'testdir/subdir1'))
# Expected output: ['a.c']


''' Test case 3: Sub directory NOT containing .c file '''
print(find_files('.c', 'testdir/subdir2'))
# Expected output: []
