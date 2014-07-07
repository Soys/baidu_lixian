# -*- coding: utf-8 -*-
'''
Created on 2014/07/05

@author: deadblue
'''

from baidupan import command, context
import readline

def completer(prefix, index):
    # TODO: 实现自动完成
    # 需要每个命令上增加接口，暂不实现
    return None

class Console():
    def __init__(self):
        # 绑定readline
        readline.parse_and_bind('tab: complete')
        readline.set_completer(completer)
    def run(self):
        while 1:
            prompt = 'YunPan:%s> ' % context.get(context.CWD)
            line = raw_input(prompt)
            if line == 'exit':
                break
            else:
                pos = line.find(' ')
                cmd = line if pos < 0 else line[0:pos]
                arg = None if pos < 0 else line[pos+1:]
                cmd = command.manager.get_command(cmd)
                if cmd:
                    cmd.execute(arg)
                else:
                    print 'invalid command'
        print 'baidupan_cli exit!'
