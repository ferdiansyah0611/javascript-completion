import sublime, re, os
import sublime_plugin

from .completions import completions
from .completion.string import string
from .completion.console import console
from .completion.array import array, array_prototype
from .completion.date import date_prototype
from .completion.keyword import keyword
from .dataset.dom import dom
from .dataset.window import window

class JavascriptCommand(sublime_plugin.EventListener):
	folder = ''
	path = ''
	def __init__(self):
		self.global_completions = [("%s \tDOM" % s, s) for s in dom] + [("%s \tWindow" % s, s) for s in window]
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
		on_string 	= view.match_selector(locations[0], "meta.string.js")
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

		# bdd
		if '// bdd' in in_line[0:2]:
			from .completion.bdd import bdd
			target = bdd + target

		# not ctrl+space
		if prefix != '':
			if on_string == False:
				target = target + completions + keyword + console + string + array + array_prototype + self.global_completions
			# typescript
			if source[2] == True or source[3] == True:
				from .completion.typescript import typescript
				target = typescript + target

			return target

		# end with dot
		elif last_line.endswith('.'):
			name_variable = last_line.split(' ')[-1][:-1]
			if name_variable.startswith('['):
				target = array
			elif name_variable.startswith("'") or name_variable.startswith('"'):
				target = string
			elif name_variable.startswith("{"):
				pass
			elif name_variable == 'Array':
				target = array_prototype
			elif name_variable == 'Date':
				target = date_prototype
			else:
				return array + array_prototype + string + date_prototype + self.global_completions
		else:
			if on_string == False:
				target = keyword + completions

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
