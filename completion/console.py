import sublime

console = [
	sublime.CompletionItem(
		"console.assert",
		annotation="console.assert",
		completion="console.assert(assertion, message)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.clear",
		annotation="console.clear",
		completion="console.clear()",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.count",
		annotation="console.count",
		completion="console.count(title)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.debug",
		annotation="console.debug",
		completion="console.debug(object)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.dir",
		annotation="console.dir",
		completion="console.dir()",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.dirxml",
		annotation="console.dirxml",
		completion="console.dirxml(node)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.error",
		annotation="console.error",
		completion="console.error($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.exception",
		annotation="console.exception",
		completion="console.exception(error$0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.group",
		annotation="console.group",
		completion="console.group($0name)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.groupCollapsed",
		annotation="console.groupCollapsed",
		completion="console.groupCollapsed($0name)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.groupEnd",
		annotation="console.groupEnd",
		completion="console.groupEnd()",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.info",
		annotation="console.info",
		completion="console.info($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.log",
		annotation="console.log",
		completion="console.log($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.profile",
		annotation="console.profile",
		completion="console.profile({$0:title})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.profileEnd",
		annotation="console.profileEnd",
		completion="console.profileEnd()",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.table",
		annotation="console.table",
		completion="console.table({$0:data})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.time",
		annotation="console.time",
		completion="console.time($0name)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.timeEnd",
		annotation="console.timeEnd",
		completion="console.timeEnd()",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.timeStamp",
		annotation="console.timeStamp",
		completion="console.timeStamp($0name)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"console.warn",
		annotation="console.warn",
		completion="console.warn($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
]