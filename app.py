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
		on_tag_js 	= view.match_selector(locations[0], "meta.tag.attributes.js")
		on_comment 	= view.match_selector(locations[0], "comment.line.double-slash.js") or view.match_selector(locations[0], "comment.block.js")
		if on_tag_js or on_comment:
			return out
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
		# interface
		if '// int' in in_line[0:5]:
			from .dataset.interface import interface
			target = target + [("%s \tInterface" % s, s) for s in interface]

		# not ctrl+space
		if prefix != '':
			if on_string == False:
				target = target + completions + keyword + console + string + array + self.global_completions
			# typescript
			if source[2] == True or source[3] == True:
				from .completion.typescript import typescript
				target = typescript + target

			return target

		# end with dot
		elif last_line.endswith('.'):
			name_variable = last_line.split(' ')[-1][:-1]
			start_fn = name_variable.find("(")
			if start_fn:
				name_variable = name_variable[name_variable.find("(") + 1:len(name_variable)]
			valid = [
				name_variable.startswith('['),
				name_variable.startswith("'") or name_variable.startswith('"'),
				name_variable.startswith("{")
			]
			if re.search(r"[a-zA-Z]+", name_variable) or True in valid:
				# symbol
				if valid[0]: return array
				elif valid[1]: return string
				elif valid[2]: return []
				# string var
				value_variable = search_reference_variable(in_line, name_variable)
				if name_variable == 'Array': return array_prototype
				elif name_variable == 'Date': return date_prototype
				elif name_variable == 'Math':
					from .dataset.math import math, constant
					target = [("%s \tMath" % s, s) for s in constant] + [("%s \tMath" % s, s + "()") for s in math]
					return target
				elif name_variable == 'process':
					from .dataset.process import process
					target = [("%s \tprocess" % s, s) for s in process]
					return target
				elif name_variable == 'performance':
					from .dataset.performance import performance
					target = [("%s \tperformance" % s, s) for s in performance]
					return target
				elif name_variable == 'Buffer':
					from .dataset.buffer import buffer
					target = [("%s \tbuffer" % s, s) for s in buffer]
					return target
				elif value_variable.startswith('Buffer.'):
					from .dataset.buffer import objects_buffer
					target = [("%s \tbuffer" % s, s) for s in objects_buffer]
					return target
				else:
					allowed = ["fs", "os", "path", "assert", "util"]
					active_module = ""
					for x in allowed:
						if value_variable.find(x) >= 0:
							active_module = x
							break
					if active_module:
						if active_module == "fs":
							from .dataset.fs import fs
							target = [("%s \tfilesystem" % s, s) for s in fs]
							return target
						elif active_module == "os":
							from .dataset.os import os_data
							target = [("%s \tos" % s, s) for s in os_data]
							return target
						elif active_module == "path":
							from .dataset.paths import paths
							target = [("%s \tpath" % s, s) for s in paths]
							return target
						elif active_module == "assert":
							from .dataset.assertion import assertion
							target = [("%s \tassert" % s, s) for s in assertion]
							return target
						elif active_module == "util":
							from .dataset.utils import utils
							target = [("%s \tutil" % s, s) for s in utils]
							return target
					else:
						return array + string + self.global_completions
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

def search_reference_variable(line, name_variable):
	line.reverse()
	value = ""
	position = 0
	for text in line:
		if position > 100: break
		check = re.search(r"(var|let|const) {0} = (.+)".format(name_variable), text)
		if check:
			value = check.groups()[1]
			break
	return value