#!/usr/bin/python -B
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
#
# asfreader.py -- Pelican plugin that processes ezt template Markdown through ezt and  then GitHub Flavored Markdown.
#

import os.path
import sys
import io
import re
import ezt

import pelican.plugins.signals
import pelican.readers
import pelican.settings

GFMReader = sys.modules['pelican-gfm.gfm'].GFMReader

class ASFReader(GFMReader):
    enabled = True
    """GFM-flavored Reader for the Pelican system that adds ASF data and ezt 
    generation prior to processing the GFM
    """
    file_extensions = ['ezmd', 'emd']


    def add_data(self, metadata):
        "Mix in ASF data as metadata"

        key = 'ASF_DATA'
        if key in self.settings:
            asf_data = self.settings.get(key, {})
            key = 'metadata'
            if key in asf_data:
                asf_metadata = asf_data[key]
                if asf_metadata:
                    metadata.update(asf_metadata)

    def read(self, source_path):
        "Read metadata and content, process content as ezt template, then render into HTML."

        # read content with embedded ezt - use GFMReader
        text, metadata = super().read_source(source_path)
        assert text
        assert metadata
        # supplement metadata with ASFData
        self.add_data(metadata)
        print("metadata: %s" % metadata)
        assert metadata
        # prepare ezt content as ezt template
        template = ezt.Template(compress_whitespace=0)
        template.parse(text, base_format=ezt.FORMAT_HTML)
        assert template
        # generate content from ezt template with metadata
        fp = io.StringIO()
        template.generate(fp, metadata)
        text = fp.getvalue()
        # Render the markdown into HTML
        if sys.version_info >= (3, 0):
            text = text.encode('utf-8')
            content = super().render(text).decode('utf-8')
        else:
            content = super().render(text)
        assert content

        return content, metadata


# The following are required or ezmd files are not processed
def add_readers(readers):
    readers.reader_classes['ezmd'] = ASFReader


def register():
    pelican.plugins.signals.readers_init.connect(add_readers)
