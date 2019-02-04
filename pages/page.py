import re
import config
import arrow
from datetime import datetime
from jinja2 import Markup
from pathlib import Path
from markdown import markdown
from environment import env

def get_ct_time(md_file):
    return arrow.get(md_file.stat().st_ctime, tzinfo=config.REGION).format(config.TIME_FORMAT)

def get_md_time(md_file):
    return arrow.get(md_file.stat().st_mtime,
            tzinfo=config.REGION).format(config.TIME_FORMAT)

class Page():
    def __init__(self, base_file=None, template='page.html', **kwargs):
        # self.id looks for us
        self._id = None
        self._slug = None
        self.template = template
        self._date_published = None
        self._date_modified = None
        self._category = 'Uncategorized'
        self._image = None

        # self.date_published looks for us
        self._date = None
        self._updated = None

        self.base_file = base_file
        
        if base_file:
            self.from_file(base_file) # creates initial properties and self.content

        temp =  env.get_template(self.template)
        self.html = temp.render(metadata=self, config=config, **kwargs)
        
    def from_file(self, base_file):
        matcher = r'^\w+:'
        with open(base_file) as f:
            md_content = f.readlines()
            while re.match(matcher, md_content[0]):
                line = md_content.pop(0)
                line_data = line.split(': ', 1)
                key = line_data[0].lower()
                value = line_data[-1].rstrip()
                setattr(self, f'_{key}', value)
            content = '\n'.join(md_content)
            self.content = content.strip('\n')
            self.markup = Markup(markdown(content))

        self.title = getattr(self, '_title', '')
        self.__str__ = self.content
        temp =  env.get_template(self.template)
        self.html = temp.render(metadata=self, config=config) 
        self.date_published = self.get_date_published()
        self.date_modified = self.get_date_modified()

    @property
    def id(self):
        return self._id or self._slug or self.base_file.stem
    
    def get_date_published(self):
        """Returns the value of _date_published or _date, or created_datetime from
the system if not defined. NOTE THE SYSTEM DATE IS KNOWN TO CAUSE
ISSUES WITH FILES THAT WERE COPIED OR TRANSFERRED WITHOUT THEIR
METADATA BEING TRANSFER READ AS WELL"""

        if self._date_published:
            date = arrow.get(self._date_published, config.TIME_FORMAT)

        elif self._date:
            date = arrow.get(self._date, config.TIME_FORMAT)

        else:
             date = get_ct_time(self.base_file)

        return date.format(config.TIME_FORMAT)

    def get_date_modified(self):
        """Returns the value of _date_modified or _update, or the
modified_datetime from the system if not defined. NOTE THE SYSTEM 
DATE IS KNOWN TO CAUSE ISSUES WITH FILES THAT WERE COPIED OR 
TRANSFERRED WITHOUT THEIR METADADTA BEING TRANSFERRED AS WELL"""

        if self._date_modified:
            date = arrow.get(self._date_modified, config.TIME_FORMAT)
        
        elif self._updated:
            date = arrow.get(self._date, config.TIME_FORMAT)

        else:
            date = get_md_time(self.base_file)

        return date.format('MMMM DD, YYYY HH:MM')

    @property
    def image(self):
        return self._image

