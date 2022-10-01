import sublime, re, os
import sublime_plugin

from .completions import completions
from .completion.string import string
from .completion.console import console
from .completion.array import array

class JavascriptCommand(sublime_plugin.EventListener):
	folder = ''
	path = ''
	def on_query_completions(self, view, prefix, locations):
		source = [
			view.match_selector(locations[0], "source.js"),
			view.match_selector(locations[0], "source.jsx"),
			view.match_selector(locations[0], "source.ts"),
			view.match_selector(locations[0], "source.tsx"),
			view.match_selector(locations[0], "source.mjs"),
		]
		if not True in source:
			return []

		prefix 		= prefix.lower()

		cursor 		= locations[0] - len(prefix)
		line 		= view.substr(sublime.Region(0, cursor))

		out 		= []
		target 		= []
		in_line  	= line.split('\n')
		win 		= sublime.active_window()
		path 		= win.folders()
		current 	= win.active_view().file_name()
		active 		= ''

		# suggest import
		if len(path) and (prefix == 'from' or prefix == 'require'):
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
			target = target + completions + array + string + console
		else:
			target = completions

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
					completion="require('{relative}');".format(relative=relative),
					completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
					kind=sublime.KIND_VARIABLE
				)

			return sublime.CompletionItem(
				prefix,
				annotation="" + relative,
				completion="from '{relative}';".format(relative=relative),
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
				completion = "require('{depend}');".format(depend=depend)
				if prefix == 'from':
					completion = "from '{depend}';".format(depend=depend)

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
