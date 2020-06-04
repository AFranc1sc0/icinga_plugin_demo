import nagiosplugin

class cpu_check(nagiosplugin.Resource):

    def probe(self):
        return [nagiosplugin.Metric('world', True, context='null')]


def main():
    check = nagiosplugin.Check(cpu_check())
    check.main()


if __name__=='__main__':
    main()
