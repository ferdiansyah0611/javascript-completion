import sublime, re, os
import sublime_plugin

from .completions import completions
from .completion.string import string
from .completion.console import console
from .completion.array import array

class JavascriptCommand(sublime_plugin.EventListener):
	folder = ''
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
		path 		= sublime.active_window().folders()

		# not ctrl+space
		if (prefix == 'from' or prefix == 'require') and len(path):
			file 	= self.import_file(path[0], prefix)
			dev 	= self.reading_package_json(path[0], prefix)
			target 	= file + dev

		if prefix != '':
			target = target + completions + array + string + console
		else:
			target = completions

		# bdd
		if '// bdd' in in_line[0:2]:
			from .completion.bdd import bdd
			target = bdd + target

		for comp in target:
			if comp.trigger.find(r'{prefix}'):
				out.append(comp)

		return out

	def import_file(self, path, prefix):
		self.out = []

		def search(value):
			if re.search(r"\.js$|\.jsx$|\.ts$|\.tsx$|\.mjs$", value):
				return value
		def search_dir(value):
			if value.find('.') == -1:
				return value

		def update(value):
			path_prefix = "./{value}".format(value=value)
			if self.folder != '':
				path_prefix = './{folder}/{value}'.format(folder=self.folder, value=value).replace('//', '/')

			if prefix == 'require':
				return sublime.CompletionItem(
					prefix,
					annotation="" + path_prefix,
					completion="require('{path_prefix}');".format(path_prefix=path_prefix),
					completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
					kind=sublime.KIND_VARIABLE
				)

			return sublime.CompletionItem(
				prefix,
				annotation="" + path_prefix,
				completion="from '{path_prefix}';".format(path_prefix=path_prefix),
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