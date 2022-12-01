# Javascript Completion

Javascript Completion for Sublime Text 3/4. Work in file js, jsx, ts, and tsx.

## Feature

- function
- object
- string
- array
- logic
- variable
- class
- console
- try/catch, switch/case, fetch, json, timer, module/import
- BDD
- suggestion for importing (file, dependencies)
- completion key in object
- keyword
- window, dom
- interface

## Usage

`ctrl+space` to see completions

## About BDD

By default is disabled, to enable BDD you must add comment `// bdd` on line 0 or 1.

## About Suggestion for Importing

To appear suggestion file or dependencies, try like this:

`require` then `ctrl+space`

`from` then `ctrl+space`

## About Interface

By default is disabled, to enable you must add comment `// int` on line 0/1/2/3/4/5.

## Completion key in Object

Work if value of key is string or integer

Work

```js
var users = {
	id: 'ok',
	name: '10',
	data: {
		active: '',
		last: {
			msg: 1,
			date: 1
		}
	}
};
```

write `users.` and can see all key

Doesn't Work

```js
var users = {
	id: 'ok',
	name: '10',
	data: {
		active: '',
		last: {
			msg: 1,
			function(){}
		}
	}
};
```

## String, Array, Function Completion

```js
let arr = []
let str = ''
```

write `namevariable.` then can see all object of type.