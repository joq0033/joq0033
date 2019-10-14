from TIGr import AbstractSourceReader
from TurtlePrompt import TurtlePrompt
from Parser import IntegerParser, StringParser, ArgumentParser
from TurtleDrawer import TurtleDrawer
from TkinterDrawer import TkinterDrawer


class ArgumentSourceReader(AbstractSourceReader):
    def go(self):
        result = ArgumentParser.parse(self, '')

        if result == 'g':
            print('graphics')
        elif result == 't':
            TurtlePrompt().cmdloop()
        elif result == 'k':
            TkinterDrawer().start()
        elif result == 'e':
            exit()
        else:
            print('graphics')


# if __name__ == '__main__':
#     s = ArgumentSourceReader(ArgumentParser(''))
#     s.go()
