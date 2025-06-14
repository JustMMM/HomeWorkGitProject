from io import StringIO
from network import Network
from computer import Computer
from component import CPU, Memory, Disk


def main():
    out = StringIO()
    n = Network("MISIS network")

    n.add_computer(
        Computer("server1.misis.ru")
        .add_address("192.168.1.1")
        .add_component(CPU(4, 2500))
        .add_component(Memory(16000))
    )

    n.add_computer(
        Computer("server2.misis.ru")
        .add_address("10.0.0.1")
        .add_component(CPU(8, 3200))
        .add_component(
            Disk(Disk.MAGNETIC, 2000)
            .add_partition(500, "system")
            .add_partition(1500, "data")
        )
    )

    n.print_me(out)
    print(out.getvalue())


if __name__ == "__main__":
    main()