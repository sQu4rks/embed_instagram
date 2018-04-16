# embed_instagram #

A simple [pelican](https://getpelican.com) plugin to embed instagram posts into your post. 

**Attention** right now this plugin requires internet access when rendering your posts to retrieve the code from Instagram's API. 

## Installation ##

Clone the repository into your plugin directory e.g.

```
$ git@github.com:sQu4rks/embed_instagram.git
```

and then add `embed_instagram` to your `PLUGINS` in `pelicanconf.py`.

## Usage ##

In a (Markdown) document, just add

```
This is some text

[INSTA]BhKJ0bOhurv[/INSTA]

and here is some more text
```

This will request the embedding code upon rendering the html and add a centered instagram image/video block. 

## Stuff To Do ##

* Tests
* Create a local cache of the embedding code to make rendering offline possible
