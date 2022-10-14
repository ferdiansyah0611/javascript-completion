import sublime, re, os
import sublime_plugin

from .completions import completions
from .completion.string import string
from .completion.console import console
from .completion.array import array
from .completion.keyword import keyword

class JavascriptCommand(sublime_plugin.EventListener):
	folder = ''
	path = ''
	def on_query_completions(self, view, prefix, locations):
		source 		= [
			view.match_selector(locations[0], "source.js"),
			view.match_selector(locations[0], "source.jsx"),
			view.match_selector(locations[0], "source.ts"),
			view.match_selector(locations[0], "source.tsx"),
			view.match_selector(locations[0], "source.mjs")
		]

		if not True in source:
			return []

		win 		= sublime.active_window()
		current 	= win.active_view().file_name()
		path 		= win.folders()
		prefix 		= prefix.lower()
		cursor 		= locations[0] - len(prefix)
		line 		= view.substr(sublime.Region(0, cursor))
		active 		= ''
		out 		= []
		target 		= []
		in_line  	= line.split('\n')
		last_line 	= in_line[-1]

		# suggest import
		if len(path) and (prefix == 'import' or prefix == 'require'):
			self.path 	= path[0]
			self.full_name = current

			# get folder on active views
			split_filename = current.split('\\')[:-1]
			for x in split_filename:
				if active == '':
					active = x
				else:
					active = active + '\\' + x

			self.active = active

			if active != '':
				dev 	= self.reading_package_json(self.path, prefix)
				file 	= self.import_file(self.path, prefix)
				target 	= file + dev

		# not ctrl+space
		if prefix != '':
			target = target + keyword + completions + console
			# typescript
			if source[2] == True or source[3] == True:
				from .completion.typescript import typescript
				target = typescript + target

		# end with dot
		elif last_line.endswith('.'):
			name_variable = last_line.split(' ')[-1][:-1]
			if name_variable.startswith('['):
				target = array
			elif name_variable.startswith("'") or name_variable.startswith('"'):
				target = string
			elif name_variable.startswith("{"):
				pass
			else:
				assign = []
				if name_variable:
					for x in range(0, len(in_line)):
						# check value assign
						expect = re.search(r"{name}\.[a-zA-Z]+".format(name=name_variable), in_line[x])
						if expect:
							value = expect.group()
							# unique completion
							is_allow = True
							for y in assign:
								if y.completion == value:
									is_allow = False
							
							if is_allow:
								assign = assign + [
									sublime.CompletionItem(
										value,
										annotation=value,
										completion=value,
										completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
										kind=sublime.KIND_VARIABLE
									)
								]
						# string
						if re.search(r"{name} = '".format(name=name_variable), in_line[x]):
							target = string
						# array
						if re.search(r"{name} = \[".format(name=name_variable), in_line[x]):
							target = array
						# object
						if re.search(r"{name} = {t}".format(name=name_variable, t='{'), in_line[x]):
							def recursive(in_line, x, start):
								try:
									if x > len(in_line): return
									if in_line[x].find('};') == -1:
										return recursive(in_line, x + 1, start)
									else:
										import json
										first 	= in_line[start].split(' ')[-1]
										text 	= ''
										text 	+= first

										for y in range(start + 1, x):
											text += in_line[y]

										text 	+= '}'
										text 	= text.strip().replace('\t', '').replace('{', '{"').replace(':', '":').replace(',', ',"').replace("'", '"')
										result 	= json.loads(text)
										out 	= []

										# make completion include sub object
										def reading(dictionary, left = ''):
											for key in dictionary:
												if type(dictionary[key]) == dict:
													if left != '': left = left + '.'
													reading(dictionary[key], left + key)
												else:
													text = key
													if left != '':
														text = left + '.' + key

													out.append(sublime.CompletionItem(
														text,
														annotation="key",
														completion=text,
														completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
														kind=sublime.KIND_VARIABLE
													))

										reading(result)
										return out
								except:
									pass

							result = recursive(in_line, x, x)
							if result and len(result):
								out.extend(result)

						# function
						if re.search(r"function {name}\(".format(name=name_variable), in_line[x]):
							target = [
								sublime.CompletionItem(
									"prototype",
									annotation="prototype",
									completion="prototype",
									completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
									kind=sublime.KIND_VARIABLE
								),
								sublime.CompletionItem(
									"constructor",
									annotation="constructor",
									completion="constructor",
									completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
									kind=sublime.KIND_VARIABLE
								),
							]
				
				target = assign + target
		else:
			target = keyword + completions

		# bdd
		if '// bdd' in in_line[0:2]:
			from .completion.bdd import bdd
			target = bdd + target

		for comp in target:
			if comp and comp.trigger.find(r'{prefix}'):
				out.append(comp)

		return out

	def import_file(self, path, prefix, active = ''):
		self.out = []

		def search(value):
			if re.search(r"\.js$|\.jsx$|\.ts$|\.tsx$|\.mjs$", value):
				return value
		def search_dir(value):
			if value.find('.') == -1:
				return value

		def update(value):
			full_folder = self.path + '\\' + self.folder.replace('/', '\\') + value
			relative = os.path.relpath(full_folder, self.active).replace('\\', '/')
			
			if full_folder == self.full_name:
				return None

			if not '../' in relative:
				relative = './' + relative

			if prefix == 'require':
				return sublime.CompletionItem(
					prefix,
					annotation="" + relative,
					completion="var name = require('{relative}');".format(relative=relative),
					completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
					kind=sublime.KIND_VARIABLE
				)

			return sublime.CompletionItem(
				prefix,
				annotation="" + relative,
				completion="import name from '{relative}';".format(relative=relative),
				completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
				kind=sublime.KIND_VARIABLE
			)

		def recursive(root, path, full_path = ''):
			# init
			if full_path.find('node_modules') != -1 or full_path.find('dist') != -1 or full_path.find('build') != -1:
				return
			if full_path == '':
				folder = os.listdir(root)
			else:
				folder = os.listdir(full_path)
				self.folder = self.folder + path + '/'

			# find some files
			out = list(filter(search, folder))
			self.out = self.out + list(map(update, out))

			# find subdirectory
			subdir = list(filter(search_dir, folder))
			if full_path == '':
				for subdirs in subdir:
					recursive(root, subdirs, root + '\\{0}'.format(subdirs))
			else:
				for subdirs in subdir:
					recursive(root, subdirs, full_path + '\\{0}'.format(subdirs))
			self.folder = ''

		recursive(path, '')
		return self.out

	def reading_package_json(self, path, prefix):
		try:
			import json
			out = []
			pkg = open(path + '\\package.json', 'r')
			package = json.loads(pkg.read())

			for depend in package['dependencies']:
				completion = "var name = require('{depend}');".format(depend=depend)
				if prefix == 'import':
					completion = "import name from '{depend}';".format(depend=depend)

				out.append(sublime.CompletionItem(
					prefix,
					annotation="" + depend,
					completion=completion,
					completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
					kind=sublime.KIND_VARIABLE
				))

			return out
		except:
			return []
