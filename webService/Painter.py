#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        ChatGPT.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/8 9:53
# Description:
# ------------------------------------------------------------------
import openai
import os

from utils.Constant import MODEL, KEY, BASE_URL
from utils.Logger import Logger

os.environ.get("OPENAI_API_KEY")


class Painter:
    def __init__(self):
        self.model = "dall-e-3"
        self.role = "user"
        self.key = KEY

        self.logger = Logger().get_logger()
        self.client = openai.Client(
            api_key=self.key,
            base_url=BASE_URL
        )

    def ask(self, message):
        messages = []
        image_url = None
        try:
            self.logger.info(f"start to ask, content is {messages}")

            response = self.client.images.generate(prompt=message)
            image_url = response['data'][0]['url']
            print(image_url)
        except Exception as exception:
            self.logger.error(f"create completion failed with: {exception}")
            return ""

        self.logger.info(str(image_url))
        if image_url:
            return image_url
        else:
            self.logger.error("get response failed! check internet connection please.")
            raise Exception("get response failed! check internet connection please.")


if __name__ == '__main__':
    painter = Painter()
    painter.ask("天安门前的AE86")
