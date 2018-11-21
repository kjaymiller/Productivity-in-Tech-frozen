def addMetaContent(metafile, tag, metavalue):
	with open(metafile, 'r+') as f:
		original_content = f.read()
		f.write(f'{tag} = {metavalue}\n{original_content}')
		return metavalue
