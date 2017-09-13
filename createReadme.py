#!/usr/bin/env python
''' Simple script to auto-generate the README.md file for a til project.
    NOTE: Someone who wanted to be fancy would actually use a template engine
    for this, but this seemed like a task for which it is best to only require
    python.  This is not a general purpose script, but tailored for the format
    being used for "Today I Learned" repos.
'''
from __future__ import print_function
import os

HEADER = '''# TIL

> Today I Learned

A collection of concise write-ups on small things I learn day to day across a
variety of languages and technologies. These are things that don't really
warrant a full blog post.

'''

FOOTER = '''## Usage

After creating a new entry, run `./createReadme.py > README.md` to regenerate
the readme with the new data.

## About

I shamelessly stole this idea from
[jbranchaud/til](https://github.com/jbranchaud/til) who claims to have stolen
it from others.

## Other TIL Collections

* [jbranchaud/til](https://github.com/jbranchaud/til) who claims to have stolen
* [Today I Learned by Hashrocket](https://til.hashrocket.com)
* [jwworth/til](https://github.com/jwworth/til)
* [thoughtbot/til](https://github.com/thoughtbot/til)

## License

&copy; 2017 Jim Anderson

This repository is licensed under the MIT license. See `LICENSE` for
details.'''


def get_list_of_categories():
    ''' Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" in which there are TILs.'''
    dirs = [x for x in os.listdir('.') if os.path.isdir(x) and
            '.git' not in x]
    return dirs


def get_title(til_file):
    ''' Read the file until we hit the first line that starts with a #
    indicating a title in markdown.  We'll use that as the title for this
    entry. '''
    with open(til_file) as _file:
        for line in _file:
            line = line.strip()
            if line.startswith('#'):
                return line[1:].lstrip()  # text after # and whitespace


def get_tils(category):
    ''' For a given category, get the list of TIL titles. '''
    til_files = [x for x in os.listdir(category)]
    titles = []
    for filename in til_files:
        fullname = os.path.join(category, filename)
        if (os.path.isfile(fullname)) and fullname.endswith('.md'):
            title = get_title(fullname)
            titles.append((title, fullname))
    return titles


def get_category_dict(category_names):
    categories = {}
    count = 0
    for category in category_names:
        titles = get_tils(category)
        categories[category] = titles
        count += len(titles)
    return count, categories


def print_file(category_names, count, categories):
    ''' Now we have all the information, print it out in markdown format. '''
    print(HEADER)
    print('_{0} TILs and counting..._'.format(count))
    print('''
---

### Categories
''')
    # print the list of categories with links
    for category in sorted(category_names):
        print('* [{0}](#{1})'.format(category.capitalize(), category))

    # print the section for each category
    print('''
---
''')
    for category in sorted(category_names):
        print('### {0}'.format(category.capitalize()))
        print()
        tils = categories[category]
        for (title, filename) in sorted(tils):
            print('- [{0}]({1})'.format(title, filename))
        print()

    print(FOOTER)


def create_readme():
    ''' Create a TIL README.md file with a nice index for using it directly
        from github. '''
    category_names = get_list_of_categories()
    count, categories = get_category_dict(category_names)
    print_file(category_names, count, categories)

if __name__ == '__main__':
    create_readme()
