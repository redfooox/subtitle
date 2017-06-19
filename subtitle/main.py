# -*- coding: utf-8 -*-
# __author__ = 'ihciah'
import argparse
import os
import logging
from subtitle.subtitle_downloader import SubtitleDownloader


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--version', action='version', version=SubtitleDownloader.version(),
                        help=u'Show version info.'
                        )
    parser.add_argument('-l', '--loop', action='store_true', dest='loop', default=False,
                        help=u'Watch a directory(recursive), automatically download '
                             u'subtitles when an aria2 task finishes.'
                        )
    parser.add_argument('dest', action='store', default='.',
                        help=u'The path of directory or video you need to download subtitles for.')

    params = parser.parse_args()
    if params.loop:
        if os.path.isdir(params.dest):
            logging.info(u"Running...")
            SubtitleDownloader.inotify_loop(params.dest)
        else:
            logging.error(u"The given path is invalid.")
    else:
        SubtitleDownloader.download_subtitle(params.dest)
    logging.info(u"Done. :)")

if __name__ == '__main__':
    main()
