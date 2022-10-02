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

		win 		= sublime.active_window()
		current 	= win.active_view().file_name()
		source 		= re.search(r"\.js$|\.jsx$|\.ts$|\.tsx$|\.mjs$", current)

		if source == None:
			return []

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
			group_source = source.group()
			if group_source == '.ts' or group_source == '.tsx':
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
				for x in range(0, len(in_line)):
					# string
					if re.search(r"(var|let|const) {name} = '".format(name=name_variable), in_line[x]):
						target = string
						break
					# array
					if re.search(r"(var|let|const) {name} = \[".format(name=name_variable), in_line[x]):
						target = array
						break
					# object
					if re.search(r"(var|let|const) {name} = {t}".format(name=name_variable, t='{'), in_line[x]):
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

						break

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
						break
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
