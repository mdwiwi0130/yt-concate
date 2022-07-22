from pytube import YouTube
import time

from .step import Step, StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            print('download caption for', url)
            if utils.caption_file_exists(url):
                print('found existing caption file')
                continue

            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                # print(en_caption_convert_to_srt)
            except KeyError:
                print('KeyError when downloading captions for ', url)
                continue
            except AttributeError:
                print('AttributeError when downloading captions for ', url)
                continue

            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 'seconds')
