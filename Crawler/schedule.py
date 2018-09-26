from multiprocessing import Process

from Crawler.getter import Getter


class Schedule(object):

    @staticmethod
    def schedule_getter():
        """
        定时获取代理
        """
        getter = Getter()
        getter.run()

    def run(self):
        print('Getter starting...')
        getter_process = Process(target=self.schedule_getter)
        getter_process.start()


if __name__ == '__main__':
    s = Schedule()
    s.run()
