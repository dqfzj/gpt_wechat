#!/usr/bin/env python
# coding=utf-8
# ------------------------------------------------------------------
# File Name:        ChatGPT.py
# Author:           dqfzj@foxmail.com
# Created:          2024/4/8 9:53
# Description:
# ------------------------------------------------------------------
import openai

# from utils.Constant import INPUT_CONTENT
from utils.Logger import Logger
# from webService.Handle import add_history, get_history_by_user


def decode_response(completion):
    reply_content = completion.choices[0].message.content
    return reply_content


class ChatGpt:
    def __init__(self):
        self.model = "gpt-3.5-turbo"
        self.role = "user"
        self.key = "sk-8Uqopeo5NWHQ2Uo0Ca5J9tSBOOjeaLa6kxHNlN9NqFPjgCwM"
        self.client = openai.OpenAI(
            api_key=self.key,
            base_url="https://api.chatanywhere.tech/v1"
        )

        self.logger = Logger().get_logger()

    def ask(self, msg_list):
        messages = []
        for msg in msg_list:
            if msg.tran2msg():
                messages.append(msg.tran2msg())
        completion = None
        try:
            self.logger.info(f"start to ask, content is {messages}")
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
        except Exception as exception:
            self.logger.error(f"create completion failed with: {exception}")
            return ""

        self.logger.info(str(completion))
        if completion:
            reply_content = decode_response(completion)
            return reply_content
        else:
            self.logger.error("get response failed! check internet connection please.")
            raise Exception("get response failed! check internet connection please.")

    def ask_for_stram(self, content):
        resp_content = ""
        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=[{
                    "role": self.role,
                    "content": content
                }],
                timeout=10,
                stream=True
            )
            for chunk in stream:
                if chunk.choices[0].delta is not None and chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="")
                    resp_content = resp_content.join(chunk.choices[0].delta.content)
        except Exception as exception:
            self.logger.error(f"create completion failed with: {exception}")
            return ""

#
# if __name__ == '__main__':
#     gpt = ChatGpt()
#     print("input your question:")
#     while True:
#         question = input("")
#         add_history("local_user", question, INPUT_CONTENT)
#         content = gpt.ask(get_history_by_user("local_user"))
#         try:
#             ans = gpt.ask(question)
#             print(ans)
#         except Exception as e:
#             print("exception catched: " + str(e))
