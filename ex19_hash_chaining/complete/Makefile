CC= gcc
CFLAGS= -Wall -g -std=gnu99
LD= gcc
LDFLAGS=
TARGETS= map_demo

all: $(TARGETS)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

map_demo: pair.o hash.o map.o map_demo.o
	$(LD) $(LDFLAGS) -o $@ $^

clean:
	rm -f map_demo *.o
